import dataAnalysis as da
import getData as gd
import os


#gd.get_artists_from_list("TopArtists10er.txt", "10er")

root = "D:/ateien/Uni/Wintersemester21_22/winter_2021/NLP/daten/not_analysed"
folders = list(os.walk(root))[1:]

for folder in folders:
    # folder example: ('FOLDER/3', [], ['file'])
    if not folder[2]:
        os.rmdir(folder[0])

root = "D:/ateien/Uni/Wintersemester21_22/winter_2021/NLP/daten/70er"
folders = list(os.walk(root))[1:]

for folder in folders:
    # folder example: ('FOLDER/3', [], ['file'])
    if not folder[2]:
        os.rmdir(folder[0])


#da.sentiment_analysis("70ers_lyrics/Blondie_Heart-Of-Glass.txt")
#da.copy_topicsongs("topics_70ers.csv", "lovesongs_70er/", "70ers_lyrics/", 2)
#da.copy_topicsongs("topics_60ers.csv", "lovesongs_60er/", "sixties_lyrics/", 1)
#da.copy_topicsongs("topics_00ers.csv", "lovesongs_00er/", "00ers_lyrics/", 1)
#da.copy_topicsongs("topics_10ers.csv", "lovesongs_10er/", "10ers_lyrics/", 2)
#da.sentiment_analysis("lovesongs_70er")
#da.sentiment_analysis("lovesongs_60er")
#da.sentiment_analysis("lovesongs_00er")
#da.sentiment_analysis("lovesongs_10er")

da.sentiment_analysis("70ers_lyrics")
da.sentiment_analysis("sixties_lyrics")
da.sentiment_analysis("00ers_lyrics")
da.sentiment_analysis("10ers_lyrics")
#da.sentiment_analysis("alle_songs")