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

##def No_punct(text):
##    clean = re.sub('['+string.punctuation+']', ' ', text)
##    clean = re.sub('[«»“”’…–]', ' ', clean)
##    return clean
##
##def Party_Catcher(text):
##	clean = text
##	clean = re.sub(r'\bσυ ρι ζα\b', 'συριζα', clean)
##	clean = re.sub(r'\bχ α\b', 'χα', clean)
##	clean = re.sub(r'\bν δ\b', 'νδ', clean)
##	clean = re.sub(r'\bαν ελ\b', 'ανελ', clean)
##	clean = re.sub(r'\bπα σο κ\b', 'πασοκ', clean)
##	return clean
##
##		
##def Normalize_Names(text):
##    normal = text
##    #NORMALIZE SYRIZA
##    normal = re.sub(r'\bτσιπρα\b', 'τσιπρας', normal)
##    normal = re.sub(r'\bαλεξη\b', 'αλεξης', normal)
##    normal = re.sub(r'\bπρωθυπουργο\b|\bπρωθυπουργου\b', 'πρωθυπουργος', normal)
##    normal = re.sub(r'\bπαππα\b', 'παππας', normal)
##    normal = re.sub(r'\bνικο\b|\bνικου\b', 'νικος', normal)
##    normal = re.sub(r'\bτσακαλωτο\b', 'τσακαλωτος', normal)
##    normal = re.sub(r'\bευκλειδη\b', 'ευκλειδης', normal)
##    normal = re.sub(r'\bπαπαδημουλη\b', 'παπαδημουλης', normal)
##    normal = re.sub(r'\bεφης\b', 'εφη', normal) #Αχτσιογλου άκλιτο
##    normal = re.sub(r'\bσταθακη\b', 'σταθακης', normal)
##    normal = re.sub(r'\bγιωργου\b', 'γιωργος', normal)
##    normal = re.sub(r'\bκουρουμπλη\b', 'κουρουμπλης', normal)
##    normal = re.sub(r'\bπαναγιωτη\b', 'παναγιωτης', normal)
##    normal = re.sub(r'\bδραγασακη\b', 'δραγασακης', normal)
##    normal = re.sub(r'\bγιαννη\b', 'γιαννης', normal)
##    normal = re.sub(r'\bκοτζια\b', 'κοτζιας', normal)
##    normal = re.sub(r'\bτζανακοπουλο\b', 'τζανακοπουλος', normal)
##    normal = re.sub(r'\bδημητρη\b', 'δημητρης', normal)
##    normal = re.sub(r'\bβουτση\b', 'βουτσης', normal)
##    normal = re.sub(r'\bρανιας\b', 'ρανια', normal) #Σβιγκου άκλιτο
##    normal = re.sub(r'\bπολακη\b', 'πολακης', normal)
##    normal = re.sub(r'\bπαυλου\b|\bπαυλο\b', 'παυλος', normal)
##    normal = re.sub(r'\bφωτη\b', 'φωτης', normal)
##    normal = re.sub(r'\bκουβελη\b', 'κουβελης', normal)
##    #NORMALIZE ANEL
##    normal = re.sub(r'\bανεξαρτητων ελληνων\b|\bανεξαρτητοι ελληνες\b', 'ανελ', normal)
##    normal = re.sub(r'\bκαμμενου\b|\bκαμμενο\b', 'καμμενος', normal)
##    normal = re.sub(r'\bπανου\b|\bπανο\b', 'πανος', normal)
##    normal = re.sub(r'\bμανταλενας\b', 'μανταλενα', normal) #Μυτιληναιου άκλιτο
##    normal = re.sub(r'\bκουντουρας\b', 'κουντουρα', normal)
##    normal = re.sub(r'\bελενας\b', 'ελενα', normal)
##    normal = re.sub(r'\bζουραρη\b', 'ζουραρης', normal)
##    #NORMALIZE ND
##    normal = re.sub(r'\bνεας δημοκρατιας\b|\bνεα δημοκρατια\b', 'νδ', normal)
##    normal = re.sub(r'\bμητσοτακη\b', 'μητσοτακης', normal)
##    normal = re.sub(r'\bκυριακο\b|\bκυριακου\b', 'κυριακος', normal)
##    normal = re.sub(r'\bπροεδρο\b|\bπροεδρου\b', 'προεδρος', normal)
##    normal = re.sub(r'\bγεωργιαδη\b', 'γεωργιαδης', normal)
##    normal = re.sub(r'\bαδωνι\b|\bαδωνη\b|\bαδωνις\b', 'αδωνης', normal)
##    normal = re.sub(r'\bντορας\b', 'ντορα', normal) #Μπακογιάννη άκλιτο
##    normal = re.sub(r'\bσαμαρα\b', 'σαμαρας', normal)
##    normal = re.sub(r'\bαντωνη\b', 'αντωνης', normal)
##    normal = re.sub(r'\bβοριδη\b', 'βοριδης', normal)
##    normal = re.sub(r'\bμακη\b', 'μακης', normal)
##    normal = re.sub(r'\bμαριας\b', 'μαρια', normal) #Σπυράκη άκλιτο
##    normal = re.sub(r'\bκαραμανλη\b', 'καραμανλης', normal)
##    normal = re.sub(r'\bκωστα\b', 'κωστας', normal)
##    normal = re.sub(r'\bκικιλια\b', 'κικιλιας', normal)
##    normal = re.sub(r'\bβασιλη\b', 'βασιλης', normal)
##    #NORMALIZE PASOK
##    normal = re.sub(r'\bφωφης\b', 'φωφη', normal) #Γεννηματά άκλιτο
##    normal = re.sub(r'\bευαγγελο\b|\bευαγγελου\b', 'ευαγγελος', normal)
##    normal = re.sub(r'\bβενιζελου\b|\bβενιζελο\b', 'βενιζελος', normal)
##    normal = re.sub(r'\bλοβερδο\b', 'λοβερδος', normal)
##    normal = re.sub(r'\bανδρεα\b', 'ανδρεας', normal)
##    #NORMALIZE KKE
##    normal = re.sub(r'\bκουτσουμπα\b', 'κουτσουμπας', normal)
##    normal = re.sub(r'\bδημητρη\b', 'δημητρης', normal)
##    normal = re.sub(r'\bκανελλης\b', 'δκανελλη', normal)
##    normal = re.sub(r'\bλιανας\b', 'λιανα', normal)
##    #NORMALIZE XA
##    normal = re.sub(r'\bχρυσης αυγης\b|\bχα\b', 'χρυση αυγη', normal)
##    normal = re.sub(r'\bμιχαλολιακου\b', 'μιχαλολιακος', normal)
##    normal = re.sub(r'\bνικολα\b|\bνικολαου\b', 'νικολας', normal)
##    normal = re.sub(r'\bηλια\b', 'ηλιας', normal)
##    normal = re.sub(r'\bκασιδιαρη\b', 'κασιδιαρης', normal)
##
##    normal = re.sub(r'\bκωνσταντινου\b|\bκωνσταντινο\b', 'κωνσταντινος', normal)
##    normal = re.sub(r'\bευρωπαικης ενωσης\b|\bευρωπαικη ενωση\b', 'εε', normal)
##    normal = re.sub(r'\bδιεθνες νομισματικο ταμειο\b|\bδιεθνους νομισματικου ταμειου\b', 'δντ', normal)
##    normal = re.sub(r'\bτροικας\b', 'τροικα', normal)
##    return normal
##    
##        
##def Hellenize_Names(text):
##    clean = re.sub(r'\bnovartis\b', 'νοβαρτις', text)
##    clean = re.sub(r'\bseverna makedonija\b', 'σεβερνα μακεντονιγια', clean)
##    clean = re.sub(r'\bgorna makedonija\b', 'γκορνα μακεντονιγια', clean)
##    clean = re.sub(r'\bnato\b', 'νατο', clean)
##    clean = re.sub(r'\bee\b|\beu\b', 'εε', clean)
##    clean = re.sub(r'\bimf\b', 'δντ', clean)
##    clean = re.sub(r'\bcomission\b', 'κομισιον', clean)
##    clean = re.sub(r'\beurogroup\b', 'γιουρογκρουπ', clean)
##    #F-35, F-16, Belharra, FREMM, MEKO
##    return clean
##		
##exception = ['ζω', 'δω', 'νδ', 'εε', 'χα']


stoplist = open("C:/Users/johnp/Desktop/Dissertation/stop_list.txt", 'r', encoding='utf-8')
stoplist = stoplist.readlines()
stop = []
for i in stoplist:
    i = re.sub('\ufeff', '', i)
    i = i.rstrip()
    i = pitchless(i)
    stop.append(i)



raw_documents = []
##for name in glob.glob("C:/Users/johnp/Desktop/Dissertation/ANEL Website/*"):
##    file = open (name, 'r', encoding = 'utf-8')
##    file = file.read()
##    file = file.lower()
##    file = re.sub('\ufeff', ' ', file)
##    file = file.rstrip()
##    file = re.sub(r'''(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'".,<>?«»“”‘’]))''', " ", file)
##    file = re.sub(r'\bδιαβάστε περισσότερα\b', ' ', file)
##    file = re.sub(r'\bδελτίο τύπου\b', ' ', file)
##    file = Party_Catcher(file)
##    file = No_punct(file)
##    file = Hellenize_Names(file)
##    file = Pitchless(file)
##    file = " ".join([i for i in file.split() if i not in stop])
##    file = " ".join([i for i in file.split() if len(i)>1 and i not in exception])
##    file = re.sub('[^α-ω]', ' ', file)
##    file = " ".join(file.split())
##    file = Normalize_Names(file)
##    file = word_tokenize(file)
##    raw_documents.append(file)
##    '''re.sub(' +', ' ', file) // " ".join(file.split()) // re.sub('\s\s+', ' ', file)'''
##
##for name in glob.glob("C:/Users/johnp/Desktop/Dissertation/Twitter Data/ANEL/*"):
##    file = open (name, 'r', encoding = 'utf-8')
##    file = file.readlines()
##    for tweet in file:
##        tweet = re.sub('datetime.datetime', "", tweet)
##        tweet = re.sub('[0-9]|['+string.punctuation+']',"", tweet)
##        tweet = re.sub('\ufeff', '', tweet)
##        tweet = tweet.lstrip()
##        if tweet.startswith('RT'):
##            pass
##        else:
##            tweet = re.sub(r'''(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'".,<>?«»“”‘’]))''', " ", tweet)
##            tweet = Party_Catcher(tweet)
##            tweet = No_punct(tweet)
##            tweet = Hellenize_Names(tweet)
##            tweet = tweet.lstrip()
##            tweet = tweet.lower()
##            tweet = Pitchless(tweet)
##            tweet = " ".join([i for i in tweet.split() if i not in stop])
##            tweet = " ".join([i for i in tweet.split() if len(i)>1 and i not in exception])
##            tweet = re.sub('[^α-ω]', ' ', tweet)
##            tweet = " ".join(tweet.split())
##            tweet = Normalize_Names(tweet)
##            tweet = word_tokenize(tweet)
##            raw_documents.append(tweet)

file = open("C:/Users/johnp/Desktop/Dissertation/All/ANEL.txt", 'r', encoding = 'utf-8')
file = file.read()
file = word_tokenize(file)
raw_documents.append(file)
##for name in glob.glob("C:/Users/johnp/Desktop/Dissertation/All/*"):
##    file = open (name, 'r', encoding = 'utf-8')
##    file = file.read()
##    file = word_tokenize(file)
##    raw_documents.append(file)


''' <<<<<<<<<<<<<<<<FIX THIS LEMMATIZATION
stop = set(stopwords.words('english'))
exclude = set(string.punctuation) 
lemma = WordNetLemmatizer()
def clean(doc):
    stop_free = " ".join([i for i in doc.lower().split() if i not in stop])
    punc_free = ''.join(ch for ch in stop_free if ch not in exclude)
    normalized = " ".join(lemma.lemmatize(word) for word in punc_free.split())
    return normalized

doc_clean = [clean(doc).split() for doc in doc_complete]
'''

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
