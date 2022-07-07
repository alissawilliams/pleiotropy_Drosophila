#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  2 14:04:29 2022

@author: alissawilliams
"""

# script to pull out the average probability of fixation from MultiDFE output for multiple files

import os
#os.chdir("/Users/alissawilliams/Desktop/pleiotropy_Dmelanogaster/MK_analyses/multiDFE/practice/")

# open file in which to make table of probabilities of fixation
newfile = open("devo_fixation_multiDFE_ZI_lognormal_sum.txt", "w")

# read in output file (.MAXL.out) and pull out the average probability of fixation
#filename = "example.sfs.MAXL.out"
for filename in os.listdir("."):
    if filename.endswith(".sfs.MAXL.out"):
        with open(filename) as f:
            text = f.readlines()[0].split() # read in lines as list, take first entry, get rid of white space
            fixprob = text[-1] # last element of list
            fixprobnum = fixprob.split(":")[1]
            newfile.write(filename + "\t" + fixprobnum + "\n")
    
newfile.close()
