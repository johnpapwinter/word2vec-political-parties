from __future__ import unicode_literals
from Lookup_Table_GR import LookUp


class Lemmatizer:

    def lemmatize(self, word):
        table = LookUp.Table()
        if word in table:
            word = table[word]
        return word
