# Import the DependencyMatcher class
import spacy
from spacy.matcher import DependencyMatcher
from spacy.matcher import Matcher
from spacy import displacy
import topic_modeling_functions as functs

# Create a DependencyMatcher and provide model vocabulary; 
# assign result under the variable 'dep_matcher'
nlp = spacy.load('en_core_web_sm')
doc = nlp("crash come like a lightning flash")
matcher = Matcher(vocab=nlp.vocab)
#displacy.serve(doc, style='dep')

def find_metaphern(textfiles):
    nlp = spacy.load('en_core_web_sm')
    dep_matcher = DependencyMatcher(vocab=nlp.vocab)
    dep_pattern = [{'RIGHT_ID': 'adp', 'RIGHT_ATTRS': {'LOWER': {'IN': ['as', 'like']}}},
               {'LEFT_ID': 'adp', 'REL_OP': '>', 'RIGHT_ID': 'subject', 'RIGHT_ATTRS': {'POS': 'NOUN'}},
               {'LEFT_ID': 'adp', 'REL_OP': '<', 'RIGHT_ID': 'object', 'RIGHT_ATTRS': {'POS': 'VERB'}}
              ]

    
    dep_matcher.add('like_noun', patterns=[dep_pattern])

    # Apply the DependencyMatcher to the Doc object under 'doc'; Store the result 
    # under the variable 'dep_matches'.
    dep_matches = list()
    all_matches = list()
    texts = functs.getText(textfiles, minLen=1, get_text=True)
    for text in texts:
        doc = " ".join(text)
        doc = nlp(doc)
        dep_matches = dep_matcher(doc)

        for match in dep_matches:
    
    # Take the first item in the tuple at [0] and assign it under
    # the variable 'pattern_name'. This item is a spaCy Lexeme object.
            #pattern_name = match[0]
    
    # Take the second item in the tuple at [1] and assign it under
    # the variable 'matches'. This is a list of indices referring to the
    # Doc object under 'doc' that we just matched.
            matches = match[1]
    
    # Let's unpack the matches list into variables for clarity
            try: 
                verb, adp, noun = matches[2], matches[0], matches[1]
    
                all_matches.append(str(doc[verb]) + " " + str(doc[adp]) + " " + str(doc[noun]))

            except:
                adj, noun = matches[0], matches[1]

                all_matches.append(str(doc[adj]) + " " + str(doc[noun]))

    # remove duplicates and return
    return list(dict.fromkeys(all_matches))

print(find_metaphern("70ers_lyrics/"))
print(find_metaphern("sixties_lyrics/"))
print(find_metaphern("00ers_lyrics/"))
print(find_metaphern("10ers_lyrics/"))
