import spacy
import os
import pyLDAvis.gensim_models
import gensim
import gensim.corpora as corpora
from gensim.models import CoherenceModel
import randomSong as rs
import re
import pandas as pd
from langdetect import detect
from collections import OrderedDict 

files = []

def format_topics_sentences(ldamodel, corpus, texts):
    # Init output
    sent_topics_df = pd.DataFrame()
    count = 0
    # Get main topic in each document
    for i, row in enumerate(ldamodel[corpus]):
        row = sorted(row[0], key=lambda x: (x[1]), reverse=True)
        # row = sorted(row, key=lambda x: (x[1]), reverse=True) # old line
        # Get the Dominant topic, Perc Contribution and Keywords for each document
        for j, (topic_num, prop_topic) in enumerate(row):
            if j == 0: # => dominant topic
                if prop_topic < 0.4:
                    count += 1
                    continue
                wp = ldamodel.show_topic(topic_num)
                topic_keywords = ", ".join([word for word, prop in wp])
                sent_topics_df = sent_topics_df.append(pd.Series([files[i],int(topic_num), round(prop_topic,4), topic_keywords]), ignore_index=True)
            else:
                break
    sent_topics_df.columns = ['Topic_name', 'Dominant_Topic', 'Perc_Contribution', 'Topic_Keywords']
    # Add original text to the end of the output
    #contents = pd.Series(texts)
    #files_name = pd.Series(files)
    sent_topics_df = pd.concat([sent_topics_df], axis=1)
    print(count)
    return(sent_topics_df)

def getText(path_to_source, minLen = 1, replace_nl = True, get_text = False, get_folders = False):
    # loading the English model
    nlp = spacy.load('en_core_web_sm')

    # we don't want to split words with apostrophe
    nlp.tokenizer.rules = {key: value for key, value in nlp.tokenizer.rules.items() if "'" not in key and "’" not in key and "‘" not in key}


    path_to_folder=sorted([os.path.join(path_to_source, f) for f in os.listdir(path_to_source)])

    # add as many stopwords necessary
    extra_stop = ['oh','ah', 'ohh', 'ooh', 'na', 'eeh', "da", 'dee', 'doo', 'bop','yeah','oom','ahh']


    # turning the texts into tokens:
    tokenized_corpus = []
    text = []
    
    
    for my_folder in path_to_folder:
        if get_folders:
            path_to_files=sorted([os.path.join(my_folder, f) for f in os.listdir(my_folder)])
        else:
            path_to_files = path_to_folder

        for my_file in path_to_files:
            files.append(my_file)
            with open(my_file) as f:
                text = f.readlines()


            # turn all the lines into a single string
            text = ''.join(OrderedDict.fromkeys(text))
            
            text = re.sub(r"\n", " ", text)
            text = re.sub(r"\s+", " ", text)
            text = re.sub(r"^\d.*", " ", text)
            text = re.sub(r"\[[^]]*\]", " ", text)

            # create the spacy doc object with the text all in lowercase
            doc = nlp(text.lower())


                # filtering tokens and lemmatizing
            text = []

            for word in doc:
                if get_text:
                    text.append(word.text)
                elif not word.is_stop and word.is_alpha and word.lemma_ not in extra_stop and len(word) >= minLen:
                    #print(word.lemma_)
                    text.append(word.lemma_)
            tokenized_corpus.append(text)
        if not get_folders:
            break
    print(len(tokenized_corpus))
    return tokenized_corpus

def get_ldamodel(tokenized_corpus, num_topics, visualize=False, passes=20, save= None):
    # mapping words to ids
    words_id = corpora.Dictionary(tokenized_corpus)
    words_id.filter_extremes(no_below = 5, no_above=0.6)

    # corpus becomes a bag of words
    corpus = [words_id.doc2bow(txt) for txt in tokenized_corpus]
    lda_model = gensim.models.ldamodel.LdaModel(corpus=corpus,
                                           id2word=words_id,
                                           num_topics=num_topics, 
                                           random_state=50,
                                           passes=passes,
                                           #update_every=0,
                                           #alpha = "auto",
                                           #eta = "auto",
                                           per_word_topics=True)

    
    df_topic_sents_keywords = format_topics_sentences(ldamodel=lda_model, corpus=corpus, texts=tokenized_corpus)

    # Format
    df_dominant_topic = df_topic_sents_keywords.reset_index()
    df_dominant_topic.columns = ['Topic_name', 'Document_No', 'Dominant_Topic', 'Topic_Perc_Contrib', 'Keywords']

    # Show
    #print(df_dominant_topic.head(20))

    #if get_Texts_for_topic != None:
    #    texts_topic = list()
    #    for it,element in enumerate(df_dominant_topic["Dominant_Topic"]):
    #        if int(element) == 2:
    #            texts_topic.append(list)

        
    print(lda_model.print_topics(num_words = 20))
    if visualize:
        visualize_topic(lda_model, corpus, words_id)

    if save != None:
        df_dominant_topic.to_csv(save)

    return lda_model, corpus

def visualize_topic(lda_model, corpus, words_id):
    #pyLDAvis.enable_notebook()
    p = pyLDAvis.gensim_models.prepare(lda_model,corpus,words_id)
    pyLDAvis.save_html(p, "topic_visualisation.html")
    pyLDAvis.show(p, local = False)

def find_optimal_number_topics(start, end, path, steps = 1, visualize = True, passes=20, get_folders = False):
    # checking "optimal" number of topics
    tokenized_corpus = getText(path, get_folders = get_folders)
    words_id = corpora.Dictionary(tokenized_corpus)
    words_id.filter_extremes(no_below = 5, no_above=0.6)

    # corpus becomes a bag of words
    corpus = [words_id.doc2bow(txt) for txt in tokenized_corpus]
    values = list()
    coherence = list()
    for k in range(start,end+1):
        lda_model = gensim.models.ldamodel.LdaModel(corpus=corpus,
                                               id2word=words_id,
                                               num_topics=k*steps, 
                                               random_state=50,
                                               update_every=0,
                                               alpha = "auto",
                                               eta = "auto",
                                               passes=passes,
                                               per_word_topics=True)
        #if __name__ == "__main__":
        #    freeze_support()    
#        # let's compute perplexity (lower) and coherence score (higher)
        per_lda = lda_model.log_perplexity(corpus)
        coherence_model_lda = CoherenceModel(model=lda_model, texts=tokenized_corpus, dictionary=words_id, coherence='c_v')
        coherence_lda = coherence_model_lda.get_coherence()
        print(k*steps,per_lda,coherence_lda)
        values.append(k*steps)
        coherence.append(coherence_lda)


    if (visualize and (len(values) == (end - start +1))):
        rs.plotData(values, coherence, "line", "Optimal number of Topics")

def start_topic_modeling(path, number_topics, passes=20, visualize = True, save = False, get_folders = False):
    tokenized_corpus = getText(path, get_folders=get_folders)
    lda_model, _ = get_ldamodel(tokenized_corpus,number_topics,visualize, passes, save)
    

    return lda_model