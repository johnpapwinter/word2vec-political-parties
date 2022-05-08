from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import glob, string, re


def Pitchless(text):
    clean = re.sub('[άὰᾶἀἄἂἆἁἅἃἇᾳᾴᾲᾷᾀᾄᾂᾆᾁᾅᾃᾇ]', 'α', text)
    clean = re.sub('[έὲἐἔἒἑἕἓ]', 'ε', clean)
    clean = re.sub('[ϊΐίὶῖἰἴἶἱἵἳἷ]', 'ι', clean)
    clean = re.sub('[ήὴῆἠἤἢἦἡἥἣἧῃῄῂῇᾐᾔᾒᾖᾑᾕᾓᾗ]', 'η', clean)
    clean = re.sub('[όὸὀὄὂὁὅὃ]', 'ο', clean)
    clean = re.sub('[ώὼῶὠὤὢὦὡὥὣὧῳῴῲῷᾠᾤᾢᾦᾡᾥᾣᾧ]', 'ω', clean)
    clean = re.sub('[ϋΰυύὺῦὐὔὒὖὑὕὓὗ]', 'υ', clean)
    clean = re.sub('[ῤῥ]', 'ρ', clean)
    return clean

def No_punct(text):
    clean = re.sub('['+string.punctuation+']', ' ', text)
    clean = re.sub('[«»“”’…–]', ' ', clean)
    return clean

def Normalize_Names(text):
    #NORMALIZE SYRIZA
    normal = re.sub(r'\bτσιπρα\b', 'τσιπρας', text)
    normal = re.sub(r'\bαλεξη\b', 'αλεξης', normal)
    normal = re.sub(r'\bπρωθυπουργο\b|\bπρωθυπουργου\b', 'πρωθυπουργος', normal)
    normal = re.sub(r'\bπαππα\b', 'παππας', normal)
    normal = re.sub(r'\bνικο\b|\bνικου\b', 'νικος', normal)
    normal = re.sub(r'\bτσακαλωτο\b', 'τσακαλωτος', normal)
    normal = re.sub(r'\bπαπαδημουλη\b', 'παπαδημουλης', normal)
    normal = re.sub(r'\bεφης\b', 'εφη', normal)
    normal = re.sub(r'\bσταθακη\b', 'σταθακης', normal)
    normal = re.sub(r'\bγιωργου\b', 'γιωργος', normal)
    normal = re.sub(r'\bκουρουμπλη\b', 'κουρουμπλης', normal)
    normal = re.sub(r'\bπαναγιωτη\b', 'παναγιωτης', normal)
    normal = re.sub(r'\bδραγασακη\b', 'δραγασακης', normal)
    normal = re.sub(r'\bγιαννη\b', 'γιαννης', normal)
    normal = re.sub(r'\bκοτζια\b', 'κοτζιας', normal)
    normal = re.sub(r'\bτζανακοπουλο\b', 'τζανακοπουλος', normal)
    normal = re.sub(r'\bδημητρη\b', 'δημητρης', normal)
    normal = re.sub(r'\bβουτση\b', 'βουτσης', normal)
    #NORMALIZE ANEL
    normal = re.sub(r'\bανεξαρτητων ελληνων\b|\bανεξαρτητοι ελληνες\b', 'ανελ', normal)
    normal = re.sub(r'\bκαμμενου\b|\bκαμμενο\b', 'καμμενος', normal)
    normal = re.sub(r'\bπανου\b|\bπανο\b', 'πανος', normal)
    normal = re.sub(r'\bμανταλενας\b', 'μανταλενα', normal) #Μυτιληναιου άκλιτο
    normal = re.sub(r'\bκουντουρας\b', 'κουντουρα', normal)
    normal = re.sub(r'\bελενας\b', 'ελενα', normal)
    #NORMALIZE ND
    normal = re.sub(r'\bνεας δημοκρατιας\b|\bνεα δημοκρατια\b', 'νδ', normal)
    normal = re.sub(r'\bμητσοτακη\b', 'μητσοτακης', normal)
    normal = re.sub(r'\bκυριακο\b|\bκυριακου\b', 'κυριακος', normal)
    normal = re.sub(r'\bπροεδρο\b|\bπροεδρου\b', 'προεδρος', normal)
    normal = re.sub(r'\bγεωργιαδη\b', 'γεωργιαδης', normal)
    normal = re.sub(r'\bαδωνι\b|\bαδωνη\b|\bαδωνις\b', 'αδωνης', normal)
    normal = re.sub(r'\bντορας\b', 'ντορα', normal) #Μπακογιάννη άκλιτο
    normal = re.sub(r'\bσαμαρα\b', 'σαμαρας', normal)
    normal = re.sub(r'\bαντωνη\b', 'αντωνης', normal)
    normal = re.sub(r'\bβοριδη\b', 'βοριδης', normal)
    normal = re.sub(r'\bμακη\b', 'μακης', normal)
    normal = re.sub(r'\bμαριας\b', 'μαρια', normal) #Σπυράκη άκλιτο
    normal = re.sub(r'\bκαραμανλη\b', 'καραμανλης', normal)
    normal = re.sub(r'\bκωστα\b', 'κωστας', normal)
    #NORMALIZE PASOK
    normal = re.sub(r'\bφωφης\b', 'φωφη', normal) #Γεννηματά άκλιτο
    normal = re.sub(r'\bευαγγελο\b|\bευαγγελου\b', 'ευαγγελος', normal)
    normal = re.sub(r'\bβενιζελου\b|\bβενιζελο\b', 'βενιζελος', normal)
    normal = re.sub(r'\bλοβερδο\b', 'λοβερδος', normal)
    normal = re.sub(r'\bανδρεα\b', 'ανδρεας', normal)
    #NORMALIZE KKE
    normal = re.sub(r'\bκουτσουμπα\b', 'κουτσουμπας', normal)
    normal = re.sub(r'\bδημητρη\b', 'δημητρης', normal)
    #NORMALIZE XA
    normal = re.sub(r'\bχρυσης αυγης\b|\bχα\b', 'χρυση αυγη', normal)
    normal = re.sub(r'\bμιχαλολιακου\b', 'μιχαλολιακος', normal)
    normal = re.sub(r'\bνικολα\b|\bνικολαου\b', 'νικολας', normal)
    normal = re.sub(r'\bηλια\b', 'ηλιας', normal)
    normal = re.sub(r'\bκασιδιαρη\b', 'κασιδιαρης', normal)

    normal = re.sub(r'\bκωνσταντινου\b|\bκωνσταντινο\b', 'κωνσταντινος', normal)
    return normal

exception = ['ζω', 'δω', 'νδ', 'εε', 'χα', 'δει', 'ζει', 'πω', 'πει', 'μπω', 'παω', 'φαω']

stoplist = open("C:/Users/johnp/Desktop/Dissertation/stop_list.txt", 'r', encoding='utf-8')
stoplist = stoplist.readlines()
stop = []
for i in stoplist:
    i = re.sub('\ufeff', '', i)
    i = i.rstrip()
    i = Pitchless(i)
    stop.append(i)
    

data = []
for name in glob.glob("C:/Users/johnp/Desktop/Dissertation/All/*"):
    file = open (name, 'r', encoding = 'utf-8')
    file = file.read()
    file = file.lower()
    file = re.sub('\ufeff', ' ', file)
    file = file.rstrip()
    file = re.sub(r'''(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'".,<>?«»“”‘’]))''', " ", file)
    file = re.sub(r'\bδιαβάστε περισσότερα\b', ' ', file)
    file = re.sub(r'\bδελτίο τύπου\b', ' ', file)
    file = No_punct(file)
    file = re.sub(r'\bnovartis\b', 'νοβαρτις', file)
    file = re.sub(r'\bseverna makedonija\b', 'σεβερνα μακεντονιγια', file)
    file = re.sub(r'\bgorna makedonija\b', 'γκορνα μακεντονιγια', file)
    file = Pitchless(file)
    #file = " ".join([i for i in file.split() if i not in stop])
    file = " ".join([i for i in file.split() if len(i)>1 and i not in exception])
    file = re.sub('[^α-ω]', ' ', file)
    file = " ".join(file.split())
    #file = word_tokenize(file)
    #doc_complete.append(file)
    file = Normalize_Names(file)
    data.append(file)
    print(name)





vec = TfidfVectorizer(ngram_range = (1, 4), stop_words = stop)
X = vec.fit_transform(data)
S = cosine_similarity(X)

print("ANEL\tKKE\tND\tPASOK\tSYRIZA\tXA")
print(S)



