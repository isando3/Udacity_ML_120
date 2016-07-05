# -*- coding: utf-8 -*-
"""
Created on Sat Apr 16 21:32:38 2016

@author: isando3
"""

import nltk 
#nltk.download()
from nltk.corpus import stopwords
sw = stopwords.words("english")
print len(sw)

from nltk.stem.snowball import SnowballStemmer
stemmer = SnowballStemmer("english")
print stemmer.stem("response")
