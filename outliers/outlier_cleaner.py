#!/usr/bin/python

import numpy
import heapq

def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []

    ### your code goes here
    items  = len(predictions)
    res_err = [predictions[item]-net_worths[item] for item in range(items)]
    residuals = numpy.array(res_err)
    largest_res = heapq.nlargest(9,residuals)
    for item in range(items):
        mytuple = (ages[item],net_worths[item],predictions[item]-net_worths[item])
        if (predictions[item]-net_worths[item]) not in largest_res:
            cleaned_data.append(mytuple)
    return cleaned_data

