

doc1 = open('C:/Users/johnp/Desktop/Test_files/red_storm_rising.txt', 'r', encoding='utf-8')
doc1 = doc1.read()

doc2 = open('C:/Users/johnp/Desktop/Test_files/Forsyth, Frederick (1984). The Fourth Protocol.txt', 'r', encoding='utf-8')
doc2 = doc2.read()

doc3 = open('C:/Users/johnp/Desktop/Test_files/Clancy, Tom (1984). The Hunt for Red October.txt', 'r', encoding='utf-8')
doc3 = doc3.read()

doc4 = open('C:/Users/johnp/Desktop/Test_files/Ludlum, Robert (1984). The Bourne Identity.txt', 'r', encoding='utf-8')
doc4 = doc4.read()

doc5 = open('C:/Users/johnp/Desktop/Test_files/Hackett, John (1982). The Third World War. The Untold Story.txt', 'r', encoding='utf-8')
doc5 = doc5.read()


# compile documents
#doc_complete = [doc1, doc2, doc3, doc4, doc5]
doc_complete = [doc1, doc2, doc3, doc4, doc5]

from nltk.corpus import stopwords 
from nltk.stem.wordnet import WordNetLemmatizer
import string
stop = set(stopwords.words('english'))
exclude = set(string.punctuation) 
lemma = WordNetLemmatizer()
def clean(doc):
    stop_free = " ".join([i for i in doc.lower().split() if i not in stop])
    punc_free = ''.join(ch for ch in stop_free if ch not in exclude)
    normalized = " ".join(lemma.lemmatize(word) for word in punc_free.split())
    return normalized

doc_clean = [clean(doc).split() for doc in doc_complete]

import gensim
from gensim import corpora

bigram_mod = gensim.models.Phrases(doc_clean, min_count=5, threshold=100) # higher threshold fewer phrases.
bigram = gensim.models.phrases.Phraser(bigram_mod)
doc_clean = [bigram[line] for line in doc_clean]

# Creating the term dictionary of our courpus, where every unique term is assigned an index.
dictionary = corpora.Dictionary(doc_clean)

# Converting list of documents (corpus) into Document Term Matrix using dictionary prepared above.
doc_term_matrix = [dictionary.doc2bow(doc) for doc in doc_clean]

# Creating the object for LDA model using gensim library
Lda = gensim.models.ldamodel.LdaModel

# Running and Trainign LDA model on the document term matrix.
ldamodel = Lda(doc_term_matrix, num_topics=5, id2word = dictionary, passes=50)

print(ldamodel.print_topics(num_topics=5, num_words=10))
#lda_model = gensim.models.ldamodel.LdaModel(corpus=doc_term_matrix, id2word=dictionary, num_topics=10, random_state=100, update_every=1, chunksize=100, passes=10, alpha='auto', per_word_topics=True)
#print(lda_model.print_topics(num_topics=5, num_words=10))
