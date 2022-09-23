import glob, re, string
from text_preprocessing import Text_Preprocessing

all_prop = open('C:/Users/johnp/Desktop/Dissertation/all_x.txt', 'a', encoding='utf-8')
list = []

exception = ['ζω', 'δω', 'νδ', 'εε', 'χα']

preprocessor = Text_Preprocessing()


stoplist = open("C:/Users/johnp/Desktop/Dissertation/STOP.txt", 'r', encoding='utf-8')
stoplist = stoplist.readlines()
stop = []
for i in stoplist:
    i = re.sub('\ufeff', '', i)
    i = i.rstrip()
    i = preprocessor.pitchless(i)
    stop.append(i)

# print("Loaded")

doc_complete = []
for name in glob.glob("C:/Users/johnp/Desktop/Dissertation/ANEL Website/*"):
    # for name in glob.glob("C:/Users/johnp/Desktop/Dissertation/KKE Website/*"):
    # for name in glob.glob("C:/Users/johnp/Desktop/Dissertation/ND Website/*"):
    # for name in glob.glob("C:/Users/johnp/Desktop/Dissertation/PASOK Website/*"):
    # for name in glob.glob("C:/Users/johnp/Desktop/Dissertation/SYRIZA Website/*"):
    # for name in glob.glob("C:/Users/johnp/Desktop/Dissertation/XA Website/*"):
    file = open(name, 'r', encoding='utf-8')
    file = file.read()
    file = re.sub('\ufeff', ' ', file)
    file = file.rstrip()
    file = re.sub(
        r'''(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'".,<>?«»“”‘’]))''',
        " ", file)
    file = preprocessor.no_punctuation(file)
    file = file.lower()
    file = re.sub(r'\bδιαβάστε περισσότερα\b', ' ', file)
    file = re.sub(r'\bδελτίο τύπου\b', ' ', file)
    file = preprocessor.party_catcher(file)
    file = preprocessor.hellenize_names(file)
    file = preprocessor.pitchless(file)
    file = " ".join([i for i in file.split() if i not in stop])
    file = re.sub('[^α-ω]', ' ', file)
    file = " ".join(file.split())
    file = preprocessor.normalize_names(file)
    all_prop.write(file)

# print("Website data OK")

for name in glob.glob("C:/Users/johnp/Desktop/Dissertation/Twitter Data/ANEL/*"):
    # for name in glob.glob("C:/Users/johnp/Desktop/Dissertation/Twitter Data/KKE/*"):
    # for name in glob.glob("C:/Users/johnp/Desktop/Dissertation/Twitter Data/ND/*"):
    # for name in glob.glob("C:/Users/johnp/Desktop/Dissertation/Twitter Data/PASOK/*"):
    # for name in glob.glob("C:/Users/johnp/Desktop/Dissertation/Twitter Data/SYRIZA/*"):
    # for name in glob.glob("C:/Users/johnp/Desktop/Dissertation/Twitter Data/XA/*"):
    file = open(name, 'r', encoding='utf-8')
    file = file.readlines()
    for tweet in file:
        tweet = re.sub(r'\bdatetime.datetime\b', "", tweet)
        tweet = re.sub('[0-9]|[' + string.punctuation + ']', "", tweet)
        tweet = re.sub('\ufeff', '', tweet)
        tweet = tweet.lstrip()
        if tweet.startswith('RT'):
            pass
        else:
            tweet = re.sub(
                r'''(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'".,<>?«»“”‘’]))''',
                " ", tweet)
            tweet = preprocessor.no_punctuation(tweet)
            tweet = preprocessor.party_catcher(tweet)
            tweet = preprocessor.hellenize_names(tweet)
            tweet = tweet.lstrip()
            tweet = tweet.lower()
            tweet = preprocessor.pitchless(tweet)
            tweet = " ".join([i for i in tweet.split() if i not in stop])
            tweet = re.sub('[^α-ω]', ' ', tweet)
            tweet = " ".join(tweet.split())
            tweet = preprocessor.normalize_names(tweet)
            all_prop.write(tweet)
all_prop.close()

print("Process complete")
