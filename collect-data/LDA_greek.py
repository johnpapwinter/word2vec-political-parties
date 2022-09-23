import glob
import re
import string

from nltk.tokenize import word_tokenize

from text_preprocessing import Text_Preprocessing

exception = ['ζω', 'δω', 'νδ', 'εε', 'χα']

doc_complete = []

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
    file = re.sub('[^α-ω]', ' ', file)
    file = " ".join(file.split())
    file = " ".join([i for i in file.split() if i not in stop])
    file = preprocessor.normalize_names(file)
    file = word_tokenize(file)
    doc_complete.append(file)

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
            tweet = re.sub('[^α-ω]', ' ', tweet)
            tweet = " ".join([i for i in tweet.split() if i not in stop])
            tweet = " ".join(tweet.split())
            tweet = preprocessor.normalize_names(tweet)
            tweet = word_tokenize(tweet)
            doc_complete.append(tweet)

import gensim
from gensim import corpora

doc_clean = doc_complete
bigram_mod = gensim.models.Phrases(doc_clean, min_count=5, threshold=100)  # higher threshold fewer phrases.
bigram = gensim.models.phrases.Phraser(bigram_mod)
doc_clean = [bigram[line] for line in doc_clean]

# Creating the term dictionary of our courpus, where every unique term is assigned an index.
dictionary = corpora.Dictionary(doc_clean)

# Converting list of documents (corpus) into Document Term Matrix using dictionary prepared above.
doc_term_matrix = [dictionary.doc2bow(doc) for doc in doc_clean]

# Creating the object for LDA model using gensim library
Lda = gensim.models.ldamodel.LdaModel

# Running and Trainign LDA model on the document term matrix.
ldamodel = Lda(doc_term_matrix, num_topics=4, id2word=dictionary, passes=2500)

print(ldamodel.print_topics(num_topics=4, num_words=15))
# lda_model = gensim.models.ldamodel.LdaModel(corpus=doc_term_matrix, id2word=dictionary, num_topics=10, random_state=100, update_every=1, chunksize=100, passes=10, alpha='auto', per_word_topics=True)
# print(lda_model.print_topics(num_topics=5, num_words=10))
