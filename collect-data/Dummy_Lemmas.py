import ctypes
import subprocess
from Lemmatizer_GR import Lemmatizer


file = open("C:/Users/johnp/Desktop/Dissertation/all_SYRIZA.txt", 'r', encoding = 'utf-8')
file = file.read()
temp = []
print("File open and read")
for i in file.split():
    temp.append(Lemmatizer.lemmatize(i))

k = " ".join(temp)
new = open("SYRIZA.txt", 'a', encoding = 'utf-8')
new.write(k)
new.close()

ctypes.windll.user32.MessageBoxW(0, "I'm done, mate!", "Done", 1)


#report = open("REPORT_OF_PROCESS.txt", "a", encoding = 'utf-8')
#report.write("I GUESS EVERYTHING WENT WELL, I WENT TO SLEEP")
#subprocess.call(["shutdown", "/s"])
