import random
import pandas as pd
import os
import re
from langdetect import detect

#https://www.jcchouinard.com/random-user-agent-with-python-and-beautifulsoup/
def GET_UA():
    uastrings = ["Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36",\
                "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.72 Safari/537.36",\
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10) AppleWebKit/600.1.25 (KHTML, like Gecko) Version/8.0 Safari/600.1.25",\
                "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:33.0) Gecko/20100101 Firefox/33.0",\
                "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36",\
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36",\
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/600.1.17 (KHTML, like Gecko) Version/7.1 Safari/537.85.10",\
                "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",\
                "Mozilla/5.0 (Windows NT 6.3; WOW64; rv:33.0) Gecko/20100101 Firefox/33.0",\
                "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.104 Safari/537.36"\
                ]

    return random.choice(uastrings)


def txt_to_csv(file):
    songs = pd.read_csv(file+".txt", header = None)
    songs.columns = ["place", "artist","song","year"]
    songs.to_csv(file+".csv", index = None)

def createNewFolder(name, year):
    try:
        os.mkdir(os.path.join(year,name))
        os.mkdir(os.path.join("not_analysed/",name))
        return True
    except:
        return False

def remove_not_english(source_directory):
    path_to_folder=sorted([os.path.join(source_directory, f) for f in os.listdir(source_directory)])



    # turning the texts into tokens:
    tokenized_corpus = []
    text = []
    files = []
    
    
    for my_folder in path_to_folder:
        path_to_files=sorted([os.path.join(my_folder, f) for f in os.listdir(my_folder)])

        for my_file in path_to_files:
            files.append(my_file)
            with open(my_file) as f:
                text = f.readlines()
            text = ''.join(text).replace('\n',' ')
            

            # turn all the lines into a single string
            text = ''.join(text)

            text = re.sub(r"\s+", " ", text)
            text = re.sub(r"^\d.*", " ", text)
            text = re.sub(r"\[[^]]*\]", " ", text)

            try:
                if detect(text) != 'en':
                    os.remove(my_file)
            except:
                os.remove(my_file)

remove_not_english("10er/")