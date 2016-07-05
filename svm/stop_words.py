# -*- coding: utf-8 -*-
"""
Created on Tue May 24 16:07:42 2016

@author: isando3
"""
import nltk
from nltk.corpus import stopwords
sw =stopwords.words("english")
print len(sw)

from nltk.stem.snowball import SnowballStemmer
stemmer =  SnowballStemmer("english")
print stemmer.stem("responsible")

