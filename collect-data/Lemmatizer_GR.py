from __future__ import unicode_literals
from Lookup_Table_GR import Lookup


class Lemmatizer:

    def lemmatize(word):
        table = Lookup.Table()
        if word in table:
            word = table[word]
        return word
