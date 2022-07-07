#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 13:55:17 2022

@author: alissawilliams
"""


import os

os.chdir("/Users/alissawilliams/Desktop/pleiotropy_Dmelanogaster/MK_analyses/multiDFE_round2/ZI/devo/")

# open files in which to write the SFS for each gene (syn and nonsyn in separate files)
nonsynfile = open("/Users/alissawilliams/Desktop/pleiotropy_Dmelanogaster/MK_analyses/multiDFE_sum/ZI/all_devo_nonsyn_SFS_ZI.txt", "w")
synfile = open("/Users/alissawilliams/Desktop/pleiotropy_Dmelanogaster/MK_analyses/multiDFE_sum/ZI/all_devo_syn_SFS_ZI.txt", "w")
geneidfile = open("/Users/alissawilliams/Desktop/pleiotropy_Dmelanogaster/MK_analyses/multiDFE_sum/ZI/all_devo_geneIDs_SFS_ZI.txt", "w")

for filename in os.listdir("."):
    if filename.endswith(".sfs"):
        with open(filename) as f:
            text = f.readlines() # read in full text
            geneidfile.write(filename + "\n")
            nonsynfile.write(text[1])
            synfile.write(text[2])
            
geneidfile.close()
nonsynfile.close()
synfile.close()

