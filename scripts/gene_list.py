#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 10:10:17 2021

@author: alissawilliams
"""

import os

os.chdir("/Users/alissawilliams/Desktop/pleiotropy_Dmelanogaster/compiling_CDS/")

# make list of needed gene names
geneNames = open("all_Dmel_genes.txt", "r")
geneList = []
for line in geneNames:
    linestrip = line.strip()
    geneList.append(linestrip)
    
# read through tsv file and only keep lines representing the genes in geneList
fullfile = open("dmel_orthologs_in_drosophila_species_fb_2020_02_python.tsv", "r")
newfile = open("dmel_orthologs_in_drosophila_species_fb_2020_02_geneListOnly.tsv","w")
for line in fullfile:
    linesplit = line.split()
    # if the first entry in linesplit is in geneList, write line to new file
    if linesplit[0] in geneList:
        newfile.write(line)
        
fullfile.close()
newfile.close()
        
        
# for developmental genes
        
os.chdir("/Users/alissawilliams/Desktop/pleiotropy_Dmelanogaster/compiling_CDS/devo_genes/")
        
# make list of needed gene names
geneNames = open("developmental_genes_list.txt", "r")
geneList = []
for line in geneNames:
    linestrip = line.strip()
    geneList.append(linestrip)
    
# read through tsv file and only keep lines representing the genes in geneList
fullfile = open("dmel_orthologs_in_drosophila_species_fb_2020_02_python.tsv", "r")
newfile = open("dmel_orthologs_in_drosophila_species_fb_2020_02_devogeneListOnly.tsv","w")
for line in fullfile:
    linesplit = line.split()
    # if the first entry in linesplit is in geneList, write line to new file
    if linesplit[0] in geneList:
        newfile.write(line)
        
fullfile.close()
newfile.close()





