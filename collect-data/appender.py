import glob, os, re, string
from Lemmatizer_GR import Lemmatizer

all_prop = open('C:/Users/johnp/Desktop/Dissertation/all_x.txt', 'a', encoding='utf-8')
list = []

exception = ['ζω', 'δω', 'νδ', 'εε', 'χα']

'''
def Lemmas(text):
    stoplist = open("C:/Users/johnp/Desktop/Dissertation/stop_list.txt", 'r', encoding='utf-8')
    stoplist = stoplist.readlines()
    stop = []
    for i in stoplist:
        i = re.sub('\ufeff', '', i)
        i = i.rstrip()
        #i = Pitchless(i)
        stop.append(i)
    #text = text.split()
    text = text.lower()
    text2 = []
    for i in text.split():
          text2.append(Lemmatizer.Lemmatize(i)) #= " ".join(Lemmatizer.Lemmatize(i))
    text2 = " ".join([i for i in text2 if i not in stop])
    return text2
'''


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


def no_punctuation(text):
    clean = re.sub('[' + string.punctuation + ']', ' ', text)
    clean = re.sub('[«»“”’…–]', ' ', clean)
    return clean


def party_catcher(text):
    clean = text
    clean = re.sub(r'\bσυ ρι ζα\b', 'συριζα', clean)
    clean = re.sub(r'\bχ α\b', 'χα', clean)
    clean = re.sub(r'\bν δ\b', 'νδ', clean)
    clean = re.sub(r'\bαν ελ\b', 'ανελ', clean)
    clean = re.sub(r'\bπα σο κ\b', 'πασοκ', clean)
    clean = re.sub(r'\bκ κ ε\b', 'κκε', clean)
    clean = re.sub(r'\bδ ν τ\b', 'δντ', clean)
    clean = re.sub(r'\bε ε\b', 'εε', clean)
    clean = re.sub(r'\bη π α\b', 'ηπα', clean)
    return clean


def normalize_names(text):
    normal = text
    # NORMALIZE SYRIZA
    normal = re.sub(r'\bτσιπρα\b', 'τσιπρας', normal)
    normal = re.sub(r'\bαλεξη\b', 'αλεξης', normal)
    normal = re.sub(r'\bπρωθυπουργο\b|\bπρωθυπουργου\b', 'πρωθυπουργος', normal)
    normal = re.sub(r'\bπαππα\b', 'παππας', normal)
    normal = re.sub(r'\bνικο\b|\bνικου\b', 'νικος', normal)
    normal = re.sub(r'\bτσακαλωτο\b', 'τσακαλωτος', normal)
    normal = re.sub(r'\bευκλειδη\b', 'ευκλειδης', normal)
    normal = re.sub(r'\bπαπαδημουλη\b', 'παπαδημουλης', normal)
    normal = re.sub(r'\bεφης\b', 'εφη', normal)  # Αχτσιογλου άκλιτο
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
    normal = re.sub(r'\bρανιας\b', 'ρανια', normal)  # Σβιγκου άκλιτο
    normal = re.sub(r'\bπολακη\b', 'πολακης', normal)
    normal = re.sub(r'\bπαυλου\b|\bπαυλο\b', 'παυλος', normal)
    normal = re.sub(r'\bφωτη\b', 'φωτης', normal)
    normal = re.sub(r'\bκουβελη\b', 'κουβελης', normal)
    # NORMALIZE ANEL
    normal = re.sub(r'\bανεξαρτητων ελληνων\b|\bανεξαρτητοι ελληνες\b|\bανεξαρτητους ελληνες\b', 'ανελ', normal)
    normal = re.sub(r'\bκαμμενου\b|\bκαμμενο\b', 'καμμενος', normal)
    normal = re.sub(r'\bπανου\b|\bπανο\b', 'πανος', normal)
    normal = re.sub(r'\bμανταλενας\b', 'μανταλενα', normal)  # Μυτιληναιου άκλιτο
    normal = re.sub(r'\bκουντουρας\b', 'κουντουρα', normal)
    normal = re.sub(r'\bελενας\b', 'ελενα', normal)
    normal = re.sub(r'\bζουραρη\b', 'ζουραρης', normal)
    # NORMALIZE ND
    normal = re.sub(r'\bνεας δημοκρατιας\b|\bνεα δημοκρατια\b', 'νδ', normal)
    normal = re.sub(r'\bμητσοτακη\b', 'μητσοτακης', normal)
    normal = re.sub(r'\bκυριακο\b|\bκυριακου\b', 'κυριακος', normal)
    normal = re.sub(r'\bπροεδρο\b|\bπροεδρου\b', 'προεδρος', normal)
    normal = re.sub(r'\bγεωργιαδη\b', 'γεωργιαδης', normal)
    normal = re.sub(r'\bαδωνι\b|\bαδωνη\b|\bαδωνις\b', 'αδωνης', normal)
    normal = re.sub(r'\bντορας\b', 'ντορα', normal)  # Μπακογιάννη άκλιτο
    normal = re.sub(r'\bσαμαρα\b', 'σαμαρας', normal)
    normal = re.sub(r'\bαντωνη\b', 'αντωνης', normal)
    normal = re.sub(r'\bβοριδη\b', 'βοριδης', normal)
    normal = re.sub(r'\bμακη\b', 'μακης', normal)
    normal = re.sub(r'\bμαριας\b', 'μαρια', normal)  # Σπυράκη άκλιτο
    normal = re.sub(r'\bκαραμανλη\b', 'καραμανλης', normal)
    normal = re.sub(r'\bκωστα\b', 'κωστας', normal)
    normal = re.sub(r'\bκικιλια\b', 'κικιλιας', normal)
    normal = re.sub(r'\bβασιλη\b', 'βασιλης', normal)
    normal = re.sub(r'\bβαγγελη\b', 'βαγγελης', normal)
    normal = re.sub(r'\bμειμαρακη\b', 'μειμαρακης', normal)
    # NORMALIZE PASOK
    normal = re.sub(r'\bφωφης\b', 'φωφη', normal)  # Γεννηματά άκλιτο
    normal = re.sub(r'\bευαγγελο\b|\bευαγγελου\b', 'ευαγγελος', normal)
    normal = re.sub(r'\bβενιζελου\b|\bβενιζελο\b', 'βενιζελος', normal)
    normal = re.sub(r'\bλοβερδο\b', 'λοβερδος', normal)
    normal = re.sub(r'\bανδρεα\b', 'ανδρεας', normal)
    # NORMALIZE KKE
    normal = re.sub(r'\bκουτσουμπα\b', 'κουτσουμπας', normal)
    normal = re.sub(r'\bδημητρη\b', 'δημητρης', normal)
    normal = re.sub(r'\bκανελλης\b', 'δκανελλη', normal)
    normal = re.sub(r'\bλιανας\b', 'λιανα', normal)
    # NORMALIZE XA
    normal = re.sub(r'\bχρυσης αυγης\b|\bχα\b', 'χρυση αυγη', normal)
    normal = re.sub(r'\bμιχαλολιακου\b', 'μιχαλολιακος', normal)
    normal = re.sub(r'\bνικολα\b|\bνικολαου\b', 'νικολας', normal)
    normal = re.sub(r'\bηλια\b', 'ηλιας', normal)
    normal = re.sub(r'\bκασιδιαρη\b', 'κασιδιαρης', normal)

    normal = re.sub(r'\bκωνσταντινου\b|\bκωνσταντινο\b', 'κωνσταντινος', normal)
    normal = re.sub(r'\bευρωπαικης ενωσης\b|\bευρωπαικη ενωση\b', 'εε', normal)
    normal = re.sub(r'\bδιεθνες νομισματικο ταμειο\b|\bδιεθνους νομισματικου ταμειου\b', 'δντ', normal)
    normal = re.sub(r'\bτροικας\b', 'τροικα', normal)
    return normal


def hellenize_names(text):
    clean = text
    # POLITICS
    clean = re.sub(r'\bseverna makedonija\b', 'σεβερνα μακεντονιγια', clean)
    clean = re.sub(r'\bgorna makedonija\b', 'γκορνα μακεντονιγια', clean)
    clean = re.sub(r'\bnato\b', 'νατο', clean)
    clean = re.sub(r'\bee\b|\beu\b', 'εε', clean)
    clean = re.sub(r'\bimf\b', 'δντ', clean)
    clean = re.sub(r'\bcommission\b', 'κομισιον', clean)
    clean = re.sub(r'\beurogroup\b', 'γιουρογκρουπ', clean)
    # COMPANIES
    clean = re.sub(r'\bnovartis\b', 'νοβαρτις', clean)
    clean = re.sub(r'\bexxonmobil\b|\bexonmobil\b', 'εξομομπιλ', clean)
    clean = re.sub(r'\beni\b', 'ενι', clean)
    clean = re.sub(r'\btotal\b', 'τοταλ', clean)
    clean = re.sub(r'\brepsol\b', 'ρεπσολ', clean)
    clean = re.sub(r'\bcosco\b', 'κοσκο', clean)
    clean = re.sub(r'\beldorado\b', 'ελντοραντο', clean)
    # MILITARY
    clean = re.sub(r'\bbelharra\b|\bbelh arra\b', 'μπελχαρα', clean)
    clean = re.sub(r'\bfremm\b', 'φρεμμ', clean)
    clean = re.sub(r'\bmeko\b', 'μεκο', clean)
    clean = re.sub(r'\bstandard\b|\bkortenaer\b', 'κορτναερ', clean)
    clean = re.sub(r'\bf 35\b', 'λαιτνινγκ', clean)
    clean = re.sub(r'\bf 16\b', 'βαιπερ', clean)
    clean = re.sub(r'\bs 400\b', 'εστετρακοσια', clean)
    clean = re.sub(r'\bs 300\b', 'εστριακοσια', clean)
    clean = re.sub(r'\bmirage 2000\b', 'μιραζ', clean)
    return clean


stoplist = open("C:/Users/johnp/Desktop/Dissertation/STOP.txt", 'r', encoding='utf-8')
stoplist = stoplist.readlines()
stop = []
for i in stoplist:
    i = re.sub('\ufeff', '', i)
    i = i.rstrip()
    i = pitchless(i)
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
    file = no_punctuation(file)
    # file = Lemmas(file)
    file = file.lower()
    file = re.sub(r'\bδιαβάστε περισσότερα\b', ' ', file)
    file = re.sub(r'\bδελτίο τύπου\b', ' ', file)
    file = party_catcher(file)
    file = hellenize_names(file)
    file = pitchless(file)
    file = " ".join([i for i in file.split() if i not in stop])
    file = re.sub('[^α-ω]', ' ', file)
    file = " ".join(file.split())
    # file = word_tokenize(file)
    # doc_complete.append(file)
    file = normalize_names(file)
    # file = " ".join([i for i in file.split() if len(i)>1 and i not in exception])
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
        # tweet = re.sub(r'\[datetime\.datetime\([0-9]+,\s[0-9]+,\s[0-9]+,\s[0-9]+,\s[0-9]+,\s[0-9]+\),\s\'', '', tweet)
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
            tweet = no_punctuation(tweet)
            # tweet = Lemmas(tweet)
            tweet = party_catcher(tweet)
            tweet = hellenize_names(tweet)
            # tweet = tweet.lower().lstrip()
            tweet = tweet.lstrip()
            tweet = tweet.lower()
            tweet = pitchless(tweet)
            tweet = " ".join([i for i in tweet.split() if i not in stop])
            # tweet = word_tokenize(tweet)
            # doc_complete.append(tweet)
            tweet = re.sub('[^α-ω]', ' ', tweet)
            tweet = " ".join(tweet.split())
            tweet = normalize_names(tweet)
            # tweet = " ".join([i for i in tweet.split() if len(i)>1 and i not in exception])
            all_prop.write(tweet)
all_prop.close()

print("Process complete")
