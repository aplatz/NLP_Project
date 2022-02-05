import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import random
import helper_functions as hf

def get_artists_from_list(txt_list, year):
    artists = list()
    with open(txt_list) as f:
        lines = f.read()
    lines = lines.replace("\n", ",")
    artists = lines.split(",")
    print(artists)
    artists = list(dict.fromkeys(artists))
    for artist in artists:
        try:
            #print("https://www.azlyrics.com/"+ artist[0].lower() +"/"+ artist.lower() +".html", artist)
            get_songs_from_artist("https://www.azlyrics.com/"+ artist[0].lower() +"/"+ artist.lower() +".html", artist, year)
        except:
            print(artist + "could not be found")



def get_songs_from_list(txt_list, save_in):
    hf.txt_to_csv(txt_list)
    songs = pd.read_csv(txt_list+".csv", usecols=["artist","song","year"])
    URL = "https://www.azlyrics.com/lyrics/"

    song_texts = ""
    iter = 1

    for row in songs.values:
        headers = {"User-Agent": hf.GET_UA()}
        artist = row[0].replace(" ","").lower()
        song = row[1].replace(" ","").lower()
        year = row[2]
        new_url = URL + artist + "/" + song + ".html"

        page = requests.get(new_url, headers = headers)

        soup = BeautifulSoup(page.content, "html.parser")

        try:    
            text = soup.find('div', class_="col-xs-12 col-lg-8 text-center")
            lyrics = str(text.findChildren("div")[5].getText())
            with open(save_in + row[0].replace(" ","-") +"_" +row[1].replace(" ","-") + ".txt", "w") as f:
                f.write(lyrics)

        except:
            with open("not_analysed/"+txt_list+"/missing.txt", "a") as f:
                f.write("<" + row[1] + " from " + row[0] + " could not be found>\n")
                print("error " + str(iter))

        time.sleep(random.randrange(10,60))

        if iter % 10 == 0:
            time.sleep(random.randrange(20,120))

        iter += 1

def get_songs_from_artist(source_url,artist, year = None):
    if not hf.createNewFolder(artist, year +"/"):
        print("Already exist")
        return False
    print(source_url)
    page = requests.get(source_url)
    site_url = "https://www.azlyrics.com"
    soup = BeautifulSoup(page.content, "html.parser")
    links = list()
    contents = list()
    for link in soup.find_all(class_ = "listalbum-item"):
        for var in link.find_all("a"):
            url = var.get("href")
            contents.append(var.text)
            links.append(url)

    
    for iter,link in enumerate(links):
        new_url = site_url + link
        print(new_url)

        try:    
            page = requests.get(new_url)
            soup = BeautifulSoup(page.content, "html.parser")
            text = soup.find('div', class_="col-xs-12 col-lg-8 text-center")
            lyrics = str(text.findChildren("div")[5].getText())
            with open(year + "/" + artist + "/" + contents[iter].replace(" ","-")+ ".txt", "w") as f:
                f.write(lyrics)

        except:
            with open("not_analysed/"+year + "/" + artist+"/missing.txt", "a") as f:
                f.write("<" + contents[iter] + " could not be found>\n")
                print("error " + str(iter))


        time.sleep(random.randrange(5,20))


    
    




