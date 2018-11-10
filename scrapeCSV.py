#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 22:10:55 2018

@author: aashaiavadhani
"""

from pandas import *
def findlongLatTupleCity():
    df1 = pandas.pandas.read_csv('usCitiesData.csv')
    
    #first create a dictionary with all the states with all the cities
    dataFrameStates = df1[['city', 'lat','lng']]
    
    listCity = dataFrameStates['city'].tolist()
    listLat = dataFrameStates['lat'].tolist()
    listLng = dataFrameStates['lng'].tolist()
    tupleList = tuple(zip(listLat,listLng))
    
    finalDictionary = dict(zip(listCity,tupleList))
    return finalDictionary





