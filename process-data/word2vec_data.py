import glob, re, string
from nltk.tokenize import word_tokenize
from gensim.models import Word2Vec
from gensim.models.phrases import Phraser, Phrases
import gensim
import ctypes
import subprocess


def pitchless(text):
    clean = re.sub('[άὰᾶἀἄἂἆἁἅἃἇᾳᾴᾲᾷᾀᾄᾂᾆᾁᾅᾃᾇ]', 'α', text)
    clean = re.sub('[έὲἐἔἒἑἕἓ]', 'ε', clean)
    clean = re.sub('[ϊΐίὶῖἰἴἶἱἵἳἷ]', 'ι', clean)
    clean = re.sub('[ήὴῆἠἤἢἦἡἥἣἧῃῄῂῇᾐᾔᾒᾖᾑᾕᾓᾗ]', 'η', clean)
    clean = re.sub('[όὸὀὄὂὁὅὃ]', 'ο', clean)
    clean = re.sub('[ώὼῶὠὤὢὦὡὥὣὧῳῴῲῷᾠᾤᾢᾦᾡᾥᾣᾧ]', 'ω', clean)
    clean = re.sub('[ϋΰυύὺῦὐὔὒὖὑὕὓὗ]', 'υ', clean)
    clean = re.sub('[ῤῥ]', 'ρ', clean)
    return clean



stoplist = open("C:/Users/johnp/Desktop/Dissertation/stop_list.txt", 'r', encoding='utf-8')
stoplist = stoplist.readlines()
stop = []
for i in stoplist:
    i = re.sub('\ufeff', '', i)
    i = i.rstrip()
    i = pitchless(i)
    stop.append(i)



raw_documents = []

file = open("C:/Users/johnp/Desktop/Dissertation/All/ANEL.txt", 'r', encoding = 'utf-8')
file = file.read()
file = word_tokenize(file)
raw_documents.append(file)



phrases = gensim.models.Phrases(raw_documents, common_terms = stop)
bigram = gensim.models.phrases.Phraser(phrases)




raw_documents = list(bigram[raw_documents])

print("Processing model")

model = Word2Vec(raw_documents, min_count = 3, sg = 1, hs = 1, size = 300, workers = 6, window = 10, iter = 100000) #<<<<MORE FINE-TUNING


#model.save('ALL_W11_50000')
#print("model saved")
#Word2Vec.load('name_of_model')
#print("model loaded")

ctypes.windll.user32.MessageBoxW(0, "I'm done, mate!", "Done", 1)

##documents = []
##file = open("C:/Users/johnp/Desktop/Dissertation/All/PASOK.txt", 'r', encoding = 'utf-8')
##file = file.read()
##file = word_tokenize(file)
##documents.append(file)
##phrases = gensim.models.Phrases(documents, common_terms = stop)
##bigram = gensim.models.phrases.Phraser(phrases)
##documents = list(bigram[documents])
##print("Processing model")
##model = Word2Vec(documents, min_count = 3, sg = 1, hs = 1, size = 200, workers = 6, window = 10, iter = 50000) #<<<<MORE FINE-TUNING
##model.save('PASOK_W11_50000')


#ctypes.windll.user32.MessageBoxW(0, "I'm done, mate!", "Done", 1)

#report = open("REPORT_OF_PROCESS.txt", "a", encoding = 'utf-8')
#report.write("I GUESS EVERYTHING WENT WELL, I WENT TO SLEEP, model saved")
#subprocess.call(["shutdown", "/s"])
