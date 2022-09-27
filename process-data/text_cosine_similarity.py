import glob
import re
import sys

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from text_preprocessing import Text_Preprocessing

sys.path.insert(0, "C:/Users/johnp/PycharmProjects/word2vec-political-parties/collect-data")

preprocessor = Text_Preprocessing()

exception = ['ζω', 'δω', 'νδ', 'εε', 'χα', 'δει', 'ζει', 'πω', 'πει', 'μπω', 'παω', 'φαω']

stoplist = open("C:/Users/johnp/Desktop/Dissertation/stop_list.txt", 'r', encoding='utf-8')
stoplist = stoplist.readlines()
stop = []
for i in stoplist:
    i = re.sub('\ufeff', '', i)
    i = i.rstrip()
    i = Text_Preprocessing.pitchless(i)
    stop.append(i)

data = []
for name in glob.glob("C:/Users/johnp/Desktop/Dissertation/All/*"):
    file = open(name, 'r', encoding='utf-8')
    file = file.read()
    file = file.lower()
    file = re.sub('\ufeff', ' ', file)
    file = file.rstrip()
    file = re.sub(
        r'''(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'".,<>?«»“”‘’]))''',
        " ", file)
    file = re.sub(r'\bδιαβάστε περισσότερα\b', ' ', file)
    file = re.sub(r'\bδελτίο τύπου\b', ' ', file)
    file = Text_Preprocessing.no_punctuation(file)
    file = re.sub(r'\bnovartis\b', 'νοβαρτις', file)
    file = re.sub(r'\bseverna makedonija\b', 'σεβερνα μακεντονιγια', file)
    file = re.sub(r'\bgorna makedonija\b', 'γκορνα μακεντονιγια', file)
    file = Text_Preprocessing.pitchless(file)
    file = " ".join([i for i in file.split() if len(i) > 1 and i not in exception])
    file = re.sub('[^α-ω]', ' ', file)
    file = " ".join(file.split())
    file = Text_Preprocessing.normalize_names(file)
    data.append(file)
    print(name)

vec = TfidfVectorizer(ngram_range=(1, 4), stop_words=stop)
X = vec.fit_transform(data)
S = cosine_similarity(X)

print("ANEL\tKKE\tND\tPASOK\tSYRIZA\tXA")
print(S)
