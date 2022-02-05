from multiprocessing.spawn import freeze_support
import topic_modeling_functions as tm
from multiprocessing import freeze_support
import warnings

warnings.filterwarnings('ignore')

#tm.start_topic_modeling("70ers_lyrics/", 3, passes=50, visualize = False, save = "topics_70ers.csv")
#tm.start_topic_modeling("sixties_lyrics/",3, passes = 50, visualize = True, save = "topics_60ers.csv")
#tm.start_topic_modeling("10ers_lyrics/", 28, passes = 50, visualize = True , save = "topics_10ers.csv")
#tm.start_topic_modeling("00ers_lyrics/", 3, passes = 50, visualize = False, save = "topics_00ers.csv")
#tm.start_topic_modeling("alle_songs/", 6, passes = 100, visualize = True)
#tm.start_topic_modeling("70er/", 14, passes = 50, visualize = True, save = None, get_folders = True)
tm.start_topic_modeling("70er/", 8, passes = 20, visualize = True, save = "topics_70er_bigcorpus.csv", get_folders = True)
#tm.start_topic_modeling("10er/", 8, passes = 20, visualize = True, save = None, get_folders = True)

if __name__ == "__main__":
    freeze_support
#    tm.find_optimal_number_topics(start=3,end=15,path="70er/", steps = 3, passes = 50, get_folders = True)
#    tm.find_optimal_number_topics(start=1,end=10,path="10ers_lyrics/", passes = 50)
#    tm.find_optimal_number_topics(start=2,end=10,path="sixties_lyrics/", passes = 50)
#    tm.find_optimal_number_topics(start=1,end=15,path="alle_songs/", passes = 50)