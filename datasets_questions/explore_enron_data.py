#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle
import math
import numpy
enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))
print 'The dataset has:'+ str(len(enron_data)) + 'persons'
print 'Each character has '+ str(len(enron_data["SKILLING JEFFREY K"]))+' labels'
print enron_data["SKILLING JEFFREY K"]
poi=0
nan_sal=0
n_totpay=0
n_email=0
for person in enron_data:
    #print enron_data[person]['email_address']
    if math.isnan(float(enron_data[person]['salary'])):
        nan_sal+=1
    if 'NaN' in enron_data[person]['email_address']:
        n_email+=1
    if enron_data[person]['poi']==True:
        poi+=1
    if math.isnan(float(enron_data[person]['total_stock_value'])) and enron_data[person]['poi']==True:
        n_totpay+=1
print int (poi)
print str(146-nan_sal)
print str(146-n_email)
print str(100*float(n_totpay)/float(18))
#print str(100.*float(n_totpay)/float(146))
    #print person
    #if 'SKILLING' in person:
        #print person, enron_data[person]["exercised_stock_options"]
    #print enron_data[person]['poi']
    #if enron_data[person]['poi']==True:
        #poi+=1
    #if 'JAMES' in person:
        #print person, enron_data[person]['total_stock_value']
    #if 'COLWELL' in person:
        #print person, enron_data[person]['from_this_person_to_poi']
    #if 'SKLLING' in person:
        #print person, enron_data[person][exercised_stock_options]
    #if 'SKILLING' in person or 'LAY' in person or 'FASTOW' in person:
        #print person, enron_data[person]['total_payments']
    #print max(enron_data["LAY KENNETH L"]['total_payments'],enron_data["FASTOW ANDREW S"]['total_payments'],enron_data["SKILLING JEFFREY K"]['total_payments'])
    
print poi       
