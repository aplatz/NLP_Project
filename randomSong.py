from collections import *
import spacy
from random import random
import pandas as pd
import matplotlib.pyplot as plt
from spacy.lang.en.stop_words import STOP_WORDS
from wordcloud import WordCloud 


def bigram(texts):
    result = {}
    sentence = list()
    for text in texts:
        for word in range(len(text) - 1):
            firstWord = text[word]
            secondWord = text[word+1]

            if firstWord in result:
                if secondWord in result[firstWord]:
                    result[firstWord][secondWord] = int(result[firstWord][secondWord]) +1
                else: result[firstWord][secondWord] = 1
            else:
                result[firstWord] = {secondWord: int("1")}
    
    return result

def wordOccurences(texts):
    count = 0
    result = {}
    numberTexts= {}
    for text in texts:
        temp = list()
        for ite in range(len(text)):
            count += 1
            word = str(text[ite]).lower()
            if word == " ":
                continue

            elif word in result:
                result[word] = int(result[word]) +1
            else:
                result[word] = 1
            
            if word in temp:
                continue
            elif word in numberTexts:
                    numberTexts[word] = int(numberTexts[word]) +1
            else:
                    numberTexts[word] = 1
            temp.append(word)
    
    return result,count,numberTexts

def mostUsedWords(results, times, count = 0, name = "Graph1", histogram=False):
    resultsCopy = results.copy()
    items = list()
    while times >= 0 and resultsCopy:
        word = max(resultsCopy, key = lambda x : int(results[x]))
        timesUsed = (resultsCopy[word])
        items.append((word, timesUsed))
        resultsCopy.pop(word)
        times -= 1
    if histogram:
        #words = list()
        #values = list()
        #for item in items:
        #    words.append(item[0])
        #    if count > 0: 
        #        values.append((int(item[1])/count)*100)
        #    else:
        #        values.append(int(item[1]))
        #plotData(words, values, "bar", "frequency" + name)
        getWordcloud(items, times)
    return items

def plotData(words, values, kind, name):
    df = pd.DataFrame({name: values}, index= words)
    df.plot(kind=kind)
    #plt.title()
    plt.show()

def wordsInTexts(words, texts, minNum, histogram = False, times = 20, name = ""):
    wordsTexts = words.copy()
    for word in words:
        if int(texts[word]) < minNum:
            wordsTexts.pop(word)
        else:
            wordsTexts[word] = texts[word]
    mostUsedWords(wordsTexts, times, name = "New words " +name, histogram = histogram)
    return wordsTexts


def getSimiliarWords(path, words):
    most_similar_words = dict()
    for word in words:
        nlp = spacy.load("en_core_web_sm")
        s2v = nlp.add_pipe("sense2vec")
        s2v.from_disk(path)

        word = nlp(word)

        freq = word._.s2v_freq
        vector = word._.s2v_vec
        most_similar_words[word] = word._.s2v_most_similiar(5)

def getWordcloud(words, name = " ", max_words=20):
    wordcloud = WordCloud(background_color = "white", max_words = max_words).generate_from_frequencies(words)
    plt.figure(name)
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.show()


