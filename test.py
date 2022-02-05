import dataAnalysis as da
import randomSong as rs


#matches60er = da.pattern_matching("sixties_lyrics/", ["crime", "poor"])
#matches60er = da.pattern_matching("sixties_lyrics/", ["jesus", "preacher", "losin", "evil"])
#moon von dunkel und unheimlich zu schön und hell
#matches60er = da.pattern_matching("sixties_lyrics/", ["preacher", "evil"])
matches60er = da.pattern_matching("sixties_lyrics/", ["sheep", "flame", "cardboard"])
print("sixties___________")
for match in matches60er:
    print(match, "\n")

#zweimal Freeay
#matches00er = da.pattern_matching("00ers_lyrics/", ["pill", "divide", "haunted", "haunt"])
matches00er = da.pattern_matching("00ers_lyrics/", ["ickey"])
print("00ers___________")
for match in matches00er:
    print(match, "\n")

#matches10er = da.pattern_matching("10ers_lyrics/", ["subway"])
#matches10er = da.pattern_matching("10ers_lyrics/", ["partying", "partyin", "party"])
matches10er = da.pattern_matching("10ers_lyrics/", ["home", "butterfly", "bee"])
print("10er___________")
for match in matches10er:
    print(match, "\n")

#usedWordsPFer, count, numberTextPFer = rs.wordOccurences(matches00er)
#print(usedWordsPFer)
#rs.getWordcloud(usedWordsPFer,name = "Moon in 2000-2019", max_words = 50)


#https://www.thoughtco.com/history-of-american-roads-4077442, Highway als Metapher
matches70er = da.pattern_matching("70ers_lyrics/", ["watergate"])
#matches70er = da.pattern_matching("70ers_lyrics/", ["moon", "moonlight"])
#matches70er = da.pattern_matching("70ers_lyrics/", ["watergate"])
print("seventies___________")
for match in matches70er:
    print(match, "\n")

#usedWordsPFer, count, numberTextPFer = rs.wordOccurences(matches60er)
#print(usedWordsPFer)
#rs.getWordcloud(usedWordsPFer,name = "Moon in 1960-1979", max_words = 50)

