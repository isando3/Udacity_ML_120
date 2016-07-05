# -*- coding: utf-8 -*-
"""
Created on Sat Apr 16 16:37:48 2016

@author: isando3
"""

from sklearn.preprocessing import MinMaxScaler
import numpy

weights = numpy.array([[115.0],[140.0],[175.0]])
scaler = MinMaxScaler()
rescale_weight = scaler.fit_transform(weights)
print rescale_weight