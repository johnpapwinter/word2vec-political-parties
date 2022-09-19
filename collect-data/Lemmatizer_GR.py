from __future__ import unicode_literals
from Lookup_Table_GR import Lookup


class Lemmatizer:

    def lemmatize(self):
        table = Lookup.Table()
        if self in table:
            self = table[self]
        return self
