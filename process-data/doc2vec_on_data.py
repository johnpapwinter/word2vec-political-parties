#Import all the dependencies
from gensim.models.doc2vec import Doc2Vec, TaggedDocument
from nltk.tokenize import word_tokenize
import glob, string, re

data = []
ids = []

exception = ['ζω', 'δω', 'νδ', 'εε', 'χα', 'δει', 'ζει', 'πω', 'πει', 'μπω', 'παω', 'φαω']

stoplist = open("C:/Users/johnp/Desktop/Dissertation/stop_list.txt", 'r', encoding='utf-8')
stoplist = stoplist.readlines()
stop = []
for i in stoplist:
    i = re.sub('\ufeff', '', i)
    i = i.rstrip()
    stop.append(i)

for name in glob.glob("C:/Users/johnp/Desktop/Dissertation/All_equal/*"):
    file = open (name, 'r', encoding = 'utf-8')
    file = file.read()
    ids.append(name)
    data.append(file)


#tagged_data = [TaggedDocument(words=word_tokenize(_d.lower()), tags=[str(i)]) for i, _d in enumerate(data)]
tagged_data = [TaggedDocument(words =word_tokenize(_d), tags=[str(i)]) for i, _d in enumerate(data)]


max_epochs = 1500 #INCREASE EPOCH-ITERATIONS FOR BETTER RESULTS'''
vec_size = 25
alpha = 0.025

model = Doc2Vec(vector_size=vec_size, alpha=alpha, min_alpha=0.025, min_count=1, workers = 6) #<<<<<<<<<FINE TUNE THIS''' dm =1, 
  
model.build_vocab(tagged_data)

for epoch in range(max_epochs):
    #print('iteration {0}'.format(epoch))
    model.train(tagged_data, total_examples=model.corpus_count, epochs=model.iter)
    # decrease the learning rate
    model.alpha -= 0.0002
    # fix the learning rate, no decay
    model.min_alpha = model.alpha

#model.save("d2v.model")
#print("Model Saved")


#from gensim.models.doc2vec import Doc2Vec

#model= Doc2Vec.load("d2v.model")
#to find the vector of a document which is not in training data
#f = open ("C:/Users/johnp/Desktop/Test_files/Salvatore, R.A. (1998). Paths of Darkness 01. The Silent Blade.txt", 'r', encoding = 'utf-8')
#f = f.read()
#test_data = word_tokenize("I love chatbots".lower())
#test_data = word_tokenize(f.lower())
'''test_data = word_tokenize(data[0])'''
'''v1 = model.infer_vector(test_data)'''
#print("V1_infer", v1)

# to find most similar doc using tags
'''similar_doc = model.docvecs.most_similar('0')'''
'''print("The most similar doc is:", similar_doc)'''
print(ids)

check = ['0', '1', '2', '3', '4', '5']
for i in check:
    print(model.docvecs.most_similar(i))


# to find vector of doc in training data using tags or in other words, printing the vector of document at index 1 in training data
#print(model.docvecs['1'])
