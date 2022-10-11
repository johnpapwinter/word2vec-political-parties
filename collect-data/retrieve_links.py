import glob
import re
import time
import urllib.error
from urllib.request import urlopen

from bs4 import BeautifulSoup as bs


def dict_writer(dictionary):
    x = input("Enter file name ")
    file = open(x, 'a', encoding='utf-8')
    for i, k in dictionary.items():
        file.write(str(i) + " : " + str(k))
        file.write("\n")
    file.close()



link_list = []
for name in glob.glob("C:/Users/johnp/Downloads/GR_Lost/*"):
    html = urlopen("file:///" + name)
    soup = bs(html, 'html.parser')
    for i in soup.find_all(class_="mw-category"):
        if not i.find_all(class_="CategoryTreeSection"):
            k = i
    for i in k.find_all('a'):
        i = str(i)
        i = re.sub(r'<a href="', '', i)
        i = re.sub(r'" title=".+', '', i)
        if i.startswith('/wiki/'):
            link_list.append(i)


print(len(link_list))
wikt_dict = {}
# o = []


for i in link_list[1:1000]:
    try:
        time.sleep(0.08)
        html = urlopen("https://el.wiktionary.org/" + i)
        soup = bs(html, 'html.parser')
        title = soup.title.get_text()
        title = re.sub(r'\b - Βικιλεξικό\b', '', title)
        for i in soup.find_all('tbody'):
            if "ονομαστική" in i.get_text().split():
                temp = i.get_text()
                temp = re.sub(r'[^α-ωΑ-Ωά-ώΆ-Ώΐΰ]', ' ', temp)
                temp = re.sub(r'\bονομαστική\b', ' ', temp)
                temp = re.sub(r'\bγενική\b', ' ', temp)
                temp = re.sub(r'\bαιτιατική\b', ' ', temp)
                temp = re.sub(r'\bκλητική\b', ' ', temp)
                temp = re.sub(r'\bενικός\b', ' ', temp)
                temp = re.sub(r'\bπληθυντικός\b', ' ', temp)
                temp = re.sub(r'\bπτώση\b', ' ', temp)
                # o.append(set(temp.split())
                for j in set(temp.split()):
                    if j != title:
                        wikt_dict.update({j: title})
            if "Ενεστώτας" in i.get_text().split() and "Μέση-Παθητική" not in i.get_text().split():
                temp = i.get_text()
                temp = re.sub(r'[^α-ωΑ-Ωά-ώΆ-Ώΐΰ]', ' ', temp)
                temp = re.sub(r'\bθα\b|\bνα\b', ' ', temp)
                temp = re.sub(r'\bέχω\b|\bέχεις\b|\bέχει\b|\bέχουμε\b|\bέχετε\b|\bέχουν\b|\bέχουνε\b', ' ', temp)
                temp = re.sub(r'\bείμαι\b|\bείσαι\b|\bείναι\b|\bείμαστε\b|\bείστε\b', ' ', temp)
                temp = re.sub(
                    r'\bείχα\b|\bείχες\b|\bείχε\b|\bείχαμε\b|\bείχατε\b|\bείχαν\b|\bείχανε\b|\bέχε\b|\bέχοντας\b', ' ',
                    temp)
                temp = re.sub(r'\bήμουν\b|\bήσουν\b|\bήταν\b|\bήμασταν\b|\bήσασταν\b', ' ', temp)
                temp = re.sub(r'\bΣυνοπτικοί\b|\bΕξακολουθητικοί\b|\bΣυντελεσμένοι\b|\bχρόνοι\b', ' ', temp)
                temp = re.sub(r'\bενικ\b|\bβ\b|\bα\b|\bπληθ\b|\bγ\b|\bπρόσωπα\b', ' ', temp)
                temp = re.sub(r'\bΠροστακτική\b|\bΜετοχή\b|\bΑπαρέμφατο\b|\bΥποτακτική\b', ' ', temp)
                temp = re.sub(
                    r'\bΣυνοπ\b|\bΠαρατατικός\b|\bΠαρακείμενος\b|\bΣυντελ\b|\bΜέλλ\b|\bΕξ\b|\bΥπερσυντέλικος\b|\bΕνεστώτας\b|\bΑόριστος\b',
                    ' ', temp)
                for j in set(temp.split()):
                    if j != title:
                        wikt_dict.update({j: title})
                try:
                    if "Ενεστώτας" in soup.tbody.find_next(
                            'tbody').get_text().split() and "Μέση-Παθητική" not in soup.tbody.find_next(
                            'tbody').get_text().split() and "Ευκτική" not in soup.tbody.find_next(
                            'tbody').get_text().split():
                        temp = re.sub(r'[^α-ωΑ-Ωά-ώΆ-Ώΐΰ]', ' ', temp)
                        temp = re.sub(r'\bθα\b|\bνα\b', ' ', temp)
                        temp = re.sub(r'\bέχω\b|\bέχεις\b|\bέχει\b|\bέχουμε\b|\bέχετε\b|\bέχουν\b|\bέχουνε\b', ' ',
                                      temp)
                        temp = re.sub(r'\bείμαι\b|\bείσαι\b|\bείναι\b|\bείμαστε\b|\bείστε\b', ' ', temp)
                        temp = re.sub(
                            r'\bείχα\b|\bείχες\b|\bείχε\b|\bείχαμε\b|\bείχατε\b|\bείχαν\b|\bείχανε\b|\bέχε\b|\bέχοντας\b',
                            ' ', temp)
                        temp = re.sub(r'\bήμουν\b|\bήσουν\b|\bήταν\b|\bήμασταν\b|\bήσασταν\b', ' ', temp)
                        temp = re.sub(r'\bΣυνοπτικοί\b|\bΕξακολουθητικοί\b|\bΣυντελεσμένοι\b|\bχρόνοι\b', ' ', temp)
                        temp = re.sub(r'\bενικ\b|\bβ\b|\bα\b|\bπληθ\b|\bγ\b|\bπρόσωπα\b', ' ', temp)
                        temp = re.sub(r'\bΠροστακτική\b|\bΜετοχή\b|\bΑπαρέμφατο\b|\bΥποτακτική\b', ' ', temp)
                        temp = re.sub(
                            r'\bΣυνοπ\b|\bΠαρατατικός\b|\bΠαρακείμενος\b|\bΣυντελ\b|\bΜέλλ\b|\bΕξ\b|\bΥπερσυντέλικος\b|\bΕνεστώτας\b|\bΑόριστος\b',
                            ' ', temp)
                        for j in set(temp.split()):
                            if j != title:
                                wikt_dict.update({j: title})
                except AttributeError:
                    pass
                # o.append(set(temp.split())
    except urllib.error.HTTPError:
        pass
    except urllib.error.URLError:
        pass

    # var = dd[var]
