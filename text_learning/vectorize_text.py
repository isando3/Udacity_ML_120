#!/usr/bin/python

import os
import pickle
import re
import sys

sys.path.append( "../tools/" )
from parse_out_email_text import parseOutText
from sklearn.feature_extraction.text import TfidfVectorizer

"""
    Starter code to process the emails from Sara and Chris to extract
    the features and get the documents ready for classification.

    The list of all the emails from Sara are in the from_sara list
    likewise for emails from Chris (from_chris)

    The actual documents are in the Enron email dataset, which
    you downloaded/unpacked in Part 0 of the first mini-project. If you have
    not obtained the Enron email corpus, run startup.py in the tools folder.

    The data is stored in lists and packed away in pickle files at the end.
"""


from_sara  = open("from_sara.txt", "r")
from_chris = open("from_chris.txt", "r")

from_data = []
word_data = []

### temp_counter is a way to speed up the development--there are
### thousands of emails from Sara and Chris, so running over all of them
### can take a long time
### temp_counter helps you only look at the first 200 emails in the list so you
### can iterate your modifications quicker
temp_counter = 0
#transformer = TfidfTransformer()


for name, from_person in [("sara",from_sara), ("chris", from_chris)]:
#for name, from_person in [("sara",from_sara)]:
    for path in from_person:
        #print name, path
        ### only look at first 200 emails when developing
        ### once everything is working, remove this line to run over full dataset
        temp_counter += 1
        path = os.path.join('..', path[:-1])
            #print path
        email = open(path, "r")

            ### use parseOutText to extract the text from the opened email
        words = parseOutText(email)
            #print words[3]
        stemmed_words = parseOutText(email)
        l_remove = ["sara", "shackleton", "chris", "germani"]
        #l_remove = ["sara", "shackleton", "chris", "germani", "sshacklensf",  "cgermannsf"]
        for drop_word in l_remove:
            stemmed_words = stemmed_words.replace(drop_word, "")
        
        

        word_data.append(stemmed_words)


            ### append a 0 to from_data if email is from Sara, and 1 if email is from Chris

        from_data.append(0 if name == "sara" else 1)
        email.close()
print "word_data[152] : {}".format(word_data[151])
print "emails processed"

#apply the tfidtransform
tfidf = TfidfVectorizer(stop_words='english')
print tfidf
tfidf.fit_transform(word_data)
array = tfidf.idf_
print len(array)
print 'The value is:', array[34596]
print "number of features: {}".format(len(tfidf.get_feature_names()))
from_sara.close()
from_chris.close()

pickle.dump( word_data, open("your_word_data.pkl", "w") )
pickle.dump( from_data, open("your_email_authors.pkl", "w") )





### in Part 4, do TfIdf vectorization here

from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer(stop_words = 'english')
vectorizer.fit(word_data)
print len(vectorizer.get_feature_names())
print vectorizer.get_feature_names()[34598]
