# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 16:09:00 2019

@author: daven
"""

import csv
def writemod(DataVector,file):
    with open(file, mode='a') as acsv:
        writer = csv.writer(acsv, lineterminator = '\n')
        writer.writerow(DataVector)