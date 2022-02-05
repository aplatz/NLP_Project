import spacy
from spacy.matcher import PhraseMatcher
import topic_modeling_functions as tmf
import pandas as pd
import shutil
import os
import spacy
from spacytextblob.spacytextblob import SpacyTextBlob

# Create a DependencyMatcher and provide model vocabulary; 
# assign result under the variable 'dep_matcher'


def pattern_matching(path, phrases):
    nlp = spacy.load("en_core_web_sm")
    matches = list()
    phrase_matcher = PhraseMatcher(vocab=nlp.vocab)
    texts = tmf.getText(path, replace_nl = False, get_text=True)
    patterns= [nlp(phrase) for phrase in phrases]
    phrase_matcher.add("matcher", None, *patterns)
    for text in texts:  
        string = " "
        text = string.join(text)
        text = nlp(text)
        for sent in text.sents:
            for match_id, _, _ in phrase_matcher(nlp(sent.text)):
                if nlp.vocab.strings[match_id] in ["matcher"]:
                    if sent.text not in matches:
                        matches.append(sent.text)
    return matches

def copy_topicsongs(file, destination_folder, source_folder, topic):
    songs = pd.read_csv(file, usecols=["Document_No","Dominant_Topic"])
    to_copy = list ()
    for song in songs.values:
        if int(song[1]) == topic:
            to_copy.append(int(song[0]))

    for it,file_name in enumerate(os.listdir(source_folder)):
        # construct full file path
        source = source_folder + file_name
        destination = destination_folder + file_name
        # copy only files
        if it in to_copy and os.path.isfile(source):
            shutil.copy(source, destination)

def sentiment_analysis(source_folder):
    nlp = spacy.load("en_core_web_sm")
    nlp.add_pipe('spacytextblob')
    songs = tmf.getText(source_folder, get_text = True)
    polarity = 0
    subjectivity = 0
    for song in songs:
        doc = nlp(" ".join(song))
        #print(doc._.polarity)      # Polarity: -0.125
        #print(doc._.subjectivity)  # Sujectivity: 0.9
        #print(doc._.assessments)
        polarity += doc._.polarity
        subjectivity += doc._.subjectivity
        if polarity < 0:
            print(song)
    
    num = len(songs)
    print(str(source_folder))
    print(polarity/num)
    print(subjectivity/num)



        
