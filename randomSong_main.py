import spacy 
import randomSong as rs
from pprint import pprint
import topic_modeling_functions as functs

#lyricsPFer = functs.getText("PinkFloyd/", minLen=1)
#usedWordsPFer, count, numberTextPFer = rs.wordOccurences(lyricsPFer)
#rs.getWordcloud(numberTextPFer,name = "Words in 2000", max_words = 50)

lyrics00er = functs.getText("00ers_lyrics/", minLen=1)
usedWords00er, count, numberText00er = rs.wordOccurences(lyrics00er)
#rs.mostUsedWords(usedWords10er, 20, count = count, name= "10 most used words 2010er",histogram=True)
#rs.mostUsedWords(numberText10er, 20, name= " most used words 2010er",histogram=True)
#print(rs.wordsInTexts(usedWords10er,numberText10er,3,histogram=True,times=50, name="10er"))
#rs.getWordcloud(numberText00er,name = "Words in 2000", max_words = 50)

lyrics10er = functs.getText("10ers_lyrics/", minLen=1)
usedWords10er, count, numberText10er = rs.wordOccurences(lyrics10er)
#rs.mostUsedWords(usedWords10er, 20, count = count, name= "10 most used words 2010er",histogram=True)
#rs.mostUsedWords(numberText10er, 20, name= " most used words 2010er",histogram=True)
#print(rs.wordsInTexts(usedWords10er,numberText10er,3,histogram=True,times=50, name="10er"))
bigrams = rs.bigram(lyrics10er)
#rs.mostUsedWords(bigrams["i'm"], 10, count = count, name = "Bigrams zu I'M", histogram = True)
#rs.mostUsedWords(bigrams["love"], 10, count = count, name = "Bigrams zu LOVE", histogram = True)
#rs.getWordcloud(numberText10er, "Words in 2010", 50)

lyrics70er = functs.getText("70ers_lyrics/", minLen=1)
usedWords70er, count, numberText70er = rs.wordOccurences(lyrics70er)
#rs.mostUsedWords(usedWords70er, 20, count=count, name= "10 most used words 1970er", histogram=True)
#rs.mostUsedWords(numberText70er, 20, name= " most used words 1970er",histogram=True)
#print(rs.wordsInTexts(usedWords70er,numberText70er,3,histogram=True,times=50,name="70er"))
bigrams = rs.bigram(lyrics70er)
#rs.getWordcloud(numberText70er, "Words in 1970", 50)

#rs.mostUsedWords(bigrams["i'm"], 10, count = count, name = "Bigrams zu I'M", histogram = True)
#rs.mostUsedWords(bigrams["love"], 10, count = count, name = "Bigrams zu LOVE", histogram = True)


lyrics60er = functs.getText("sixties_lyrics/", minLen=1)
usedWords60er, count, numberText60er = rs.wordOccurences(lyrics60er)
#rs.mostUsedWords(usedWords60er, 20, count = count, name = "10 most used words 1960er", histogram=True)
#rs.mostUsedWords(numberText60er, 20, name= " most used words 1960er",histogram=True)
#print(rs.wordsInTexts(usedWords60er,numberText60er,3,histogram=True,times=50,name="60er"))
bigrams = rs.bigram(lyrics60er)
#rs.getWordcloud(numberText60er,"Words in 1960",50)

#rs.mostUsedWords(bigrams["i'm"], 10, count = count, name = "Bigrams zu I'M", histogram = True)
#rs.mostUsedWords(bigrams["love"], 10, count = count, name = "Bigrams zu LOVE", histogram = True)

lyrics = functs.getText("alle_songs/", minLen=1)
usedWords, count, numberText = rs.wordOccurences(lyrics)
#rs.mostUsedWords(usedWords60er, 20, count = count, name = "10 most used words 1960er", histogram=True)
#rs.mostUsedWords(numberText60er, 20, name= " most used words 1960er",histogram=True)
#print(rs.wordsInTexts(usedWords60er,numberText60er,3,histogram=True,times=50,name="60er"))
#bigrams = rs.bigram(lyrics60er)


#rs.mostUsedWords(bigrams["i'm"], 10, count = count, name = "Bigrams zu I'M", histogram = True)
#rs.mostUsedWords(bigrams["love"], 10, count = count, name = "Bigrams zu LOVE", histogram = True)

words_all_texts = dict()
for word in numberText.keys():
    if word in usedWords00er and word in usedWords10er and word in usedWords60er and word in usedWords70er:
        if len(word) > 2:
            words_all_texts[word] = numberText[word]

rs.getWordcloud(words_all_texts,"Used words in all years",100)



newWords2000er = dict()
numberText2000er = dict()
for word in usedWords00er.keys() or word in usedWords10er.keys():
    if word not in usedWords70er and word not in usedWords60er:
        if len(word) > 2:
            try :
                newWords2000er[word] = usedWords00er[word]
                numberText2000er[word] = numberText00er[word]
            except:
                newWords2000er[word] = usedWords10er[word]
                numberText2000er[word] = numberText10er[word]

#print(rs.mostUsedWords(newWords10er, 20, name = "New words", histogram=False))

newWords_texts2000er= rs.wordsInTexts(newWords2000er,numberText2000er,2,False,times=100)
rs.getWordcloud(newWords_texts2000er,"New words in 2000",50)


newWords19er = dict()
numberText19er = dict()
for word in usedWords60er.keys() or word in usedWords70er.keys():
    if word not in usedWords10er and word not in usedWords00er:
        if len(word) > 2:
            try :
                newWords19er[word] = usedWords60er[word]
                numberText19er[word] = numberText60er[word]
            except:
                newWords19er[word] = usedWords70er[word]
                numberText19er[word] = numberText70er[word]

#print(rs.mostUsedWords(newWords10er, 20, name = "New words", histogram=False))

newWords_texts19er= rs.wordsInTexts(newWords19er,numberText19er,2,False,times=100)
rs.getWordcloud(newWords_texts19er,"New words in 1900",50)

newWords10er = dict()
for word in usedWords10er.keys():
    if word not in usedWords70er and word not in usedWords60er and word not in usedWords00er:
        if len(word) > 2:
            newWords10er[word] = usedWords10er[word]

#print(rs.mostUsedWords(newWords10er, 20, name = "New words", histogram=False))
newWords_texts10er=rs.wordsInTexts(newWords10er,numberText10er,2,False,times=100)
rs.getWordcloud(newWords_texts10er,"New words in 2010",50)

newWords70er = dict()
for word in usedWords70er.keys():
    if word not in usedWords10er and word not in usedWords00er and word not in usedWords60er:
        if len(word) > 2:
            newWords70er[word] = usedWords70er[word]

#rs.mostUsedWords(newWords70er, 20, name = "New words", histogram=True)

newWords_texts70er = rs.wordsInTexts(newWords70er,numberText70er,2,False,times=100)
rs.getWordcloud(newWords_texts70er,"New words in 1970",50)

newWords60er = dict()
for word in usedWords60er.keys():
    if word not in usedWords10er and word not in usedWords00er and word not in usedWords70er:
        if len(word) > 2:
            newWords60er[word] = usedWords60er[word]

#rs.mostUsedWords(newWords60er, 20, name = "New words", histogram=True)

newWords_texts60er = rs.wordsInTexts(newWords60er,numberText60er,2,False,times=100)
rs.getWordcloud(newWords_texts60er,"New words in 1960",50)

#print(rs.getSimiliarWords("/alle_songs", "crime"))


