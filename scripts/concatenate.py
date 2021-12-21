#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21 10:24:40 2021

@author: alissawilliams
"""

# script to concatenate aligned files for use in PAML (with codeml in codon space specifically)

import os
from Bio import SeqIO

#os.chdir("/Users/alissawilliams/Desktop/pleiotropy_Dmelanogaster/paml/")
os.chdir("/data/atate_lab/willa27/pleiotropy_Dmel/all_12_species/seqfiles_developmental_genes_edited")

# set up accumulators 
totallen = 0 # total length of final alignment
seqlenlist = [] # list of sequence lengths
numgenes = 0 # number of genes in folder
danaseq = "" # initiate empty string for each species that will contain full concatenated sequence
dereseq = ""
dgriseq = ""
dmelseq = ""
dmojseq = ""
dperseq = ""
dpseseq = ""
dsecseq = ""
dsimseq = ""
dvirseq = ""
dwilseq = ""
dyakseq = ""

# go through every fasta file in folder. extension and folder can be changed as needed
#for filename in os.listdir("practice_concat"):
for filename in os.listdir("trimmed"):
    if filename.endswith(".fas"):
        numgenes = numgenes + 1
        # make dictionary containing sequences with attached IDs
        #seqdict = SeqIO.to_dict(SeqIO.parse("./practice_concat/"+filename, "fasta"))
        seqdict = SeqIO.to_dict(SeqIO.parse("./trimmed/"+filename, "fasta"))
        # get length of alignment by pulling out one of the dictionary entries (doesn't matter which one)
        firstkey = list(seqdict.keys())[0]
        firstseq = str(seqdict[firstkey].seq)
        seqlen = len(firstseq)
        totallen = totallen + seqlen
        seqlenlist.append(seqlen)
        # look for Dana in seqdict
        searchkey = "Dana" 
        res = [val for key, val in seqdict.items() if searchkey in key]
        if res != []: # if res is not empty:
            resid = str(res).split(",")[2]
            resid = resid.split("=")[1]
            resid = resid.split("'")[1]
            resseq = str(seqdict[resid].seq)
            danaseq = danaseq + resseq
        else: # if res is empty
            emptyseq = "-" * seqlen
            danaseq = danaseq + emptyseq
        # look for Dere in seqdict
        searchkey = "Dere" 
        res = [val for key, val in seqdict.items() if searchkey in key]
        if res != []: # if res is not empty:
            resid = str(res).split(",")[2]
            resid = resid.split("=")[1]
            resid = resid.split("'")[1]
            resseq = str(seqdict[resid].seq)
            dereseq = dereseq + resseq
        else: # if res is empty
            emptyseq = "-" * seqlen
            dereseq = dereseq + emptyseq
        # look for Dgri in seqdict
        searchkey = "Dgri" 
        res = [val for key, val in seqdict.items() if searchkey in key]
        if res != []: # if res is not empty:
            resid = str(res).split(",")[2]
            resid = resid.split("=")[1]
            resid = resid.split("'")[1]
            resseq = str(seqdict[resid].seq)
            dgriseq = dgriseq + resseq
        else: # if res is empty
            emptyseq = "-" * seqlen
            dgriseq = dgriseq + emptyseq
        # look for Dmel in seqdict
        searchkey = "Dmel" 
        res = [val for key, val in seqdict.items() if searchkey in key]
        if res != []: # if res is not empty:
            resid = str(res).split(",")[2]
            resid = resid.split("=")[1]
            resid = resid.split("'")[1]
            resseq = str(seqdict[resid].seq)
            dmelseq = dmelseq + resseq
        else: # if res is empty
            emptyseq = "-" * seqlen
            dmelseq = dmelseq + emptyseq
        # look for Dmoj in seqdict
        searchkey = "Dmoj" 
        res = [val for key, val in seqdict.items() if searchkey in key]
        if res != []: # if res is not empty:
            resid = str(res).split(",")[2]
            resid = resid.split("=")[1]
            resid = resid.split("'")[1]
            resseq = str(seqdict[resid].seq)
            dmojseq = dmojseq + resseq
        else: # if res is empty
            emptyseq = "-" * seqlen
            dmojseq = dmojseq + emptyseq
        # look for Dper in seqdict
        searchkey = "Dper" 
        res = [val for key, val in seqdict.items() if searchkey in key]
        if res != []: # if res is not empty:
            resid = str(res).split(",")[2]
            resid = resid.split("=")[1]
            resid = resid.split("'")[1]
            resseq = str(seqdict[resid].seq)
            dperseq = dperseq + resseq
        else: # if res is empty
            emptyseq = "-" * seqlen
            dperseq = dperseq + emptyseq
        # look for Dpse in seqdict
        searchkey = "Dpse" 
        res = [val for key, val in seqdict.items() if searchkey in key]
        if res != []: # if res is not empty:
            resid = str(res).split(",")[2]
            resid = resid.split("=")[1]
            resid = resid.split("'")[1]
            resseq = str(seqdict[resid].seq)
            dpseseq = dpseseq + resseq
        else: # if res is empty
            emptyseq = "-" * seqlen
            dpseseq = dpseseq + emptyseq
        # look for Dsec in seqdict
        searchkey = "Dsec" 
        res = [val for key, val in seqdict.items() if searchkey in key]
        if res != []: # if res is not empty:
            resid = str(res).split(",")[2]
            resid = resid.split("=")[1]
            resid = resid.split("'")[1]
            resseq = str(seqdict[resid].seq)
            dsecseq = dsecseq + resseq
        else: # if res is empty
            emptyseq = "-" * seqlen
            dsecseq = dsecseq + emptyseq
        # look for Dsim in seqdict
        searchkey = "Dsim" 
        res = [val for key, val in seqdict.items() if searchkey in key]
        if res != []: # if res is not empty:
            resid = str(res).split(",")[2]
            resid = resid.split("=")[1]
            resid = resid.split("'")[1]
            resseq = str(seqdict[resid].seq)
            dsimseq = dsimseq + resseq
        else: # if res is empty
            emptyseq = "-" * seqlen
            dsimseq = dsimseq + emptyseq
        # look for Dvir in seqdict
        searchkey = "Dvir" 
        res = [val for key, val in seqdict.items() if searchkey in key]
        if res != []: # if res is not empty:
            resid = str(res).split(",")[2]
            resid = resid.split("=")[1]
            resid = resid.split("'")[1]
            resseq = str(seqdict[resid].seq)
            dvirseq = dvirseq + resseq
        else: # if res is empty
            emptyseq = "-" * seqlen
            dvirseq = dvirseq + emptyseq
        # look for Dwil in seqdict
        searchkey = "Dwil" 
        res = [val for key, val in seqdict.items() if searchkey in key]
        if res != []: # if res is not empty:
            resid = str(res).split(",")[2]
            resid = resid.split("=")[1]
            resid = resid.split("'")[1]
            resseq = str(seqdict[resid].seq)
            dwilseq = dwilseq + resseq
        else: # if res is empty
            emptyseq = "-" * seqlen
            dwilseq = dwilseq + emptyseq
        # look for Dyak in seqdict
        searchkey = "Dyak" 
        res = [val for key, val in seqdict.items() if searchkey in key]
        if res != []: # if res is not empty:
            resid = str(res).split(",")[2]
            resid = resid.split("=")[1]
            resid = resid.split("'")[1]
            resseq = str(seqdict[resid].seq)
            dyakseq = dyakseq + resseq
        else: # if res is empty
            emptyseq = "-" * seqlen
            dyakseq = dyakseq + emptyseq

# now assemble new concatenated file
#newfile = open("practice.txt", "w")
newfile = open("concat_devo_genes.txt", "w")
# first line
newfile.write("12 " + str(totallen) + " G\n")
# second line 
newfile.write("G" + str(numgenes))
for length in seqlenlist:
    newfile.write(" ")
    newfile.write(str(length//3)) # int division. all of these should already be multiples of 3
newfile.write("\n")
newfile.write("Drosophila_ananassae\n")
newfile.write(danaseq + "\n")
newfile.write("Drosophila_erecta\n")
newfile.write(dereseq + "\n")
newfile.write("Drosophila_grimshawi\n")
newfile.write(dgriseq + "\n")
newfile.write("Drosophila_melanogaster\n")
newfile.write(dmelseq + "\n")
newfile.write("Drosophila_mojavensis\n")
newfile.write(dmojseq + "\n")
newfile.write("Drosophila_persimilis\n")
newfile.write(dperseq + "\n")
newfile.write("Drosophila_pseudoobscura\n")
newfile.write(dpseseq + "\n")
newfile.write("Drosophila_sechellia\n")
newfile.write(dsecseq + "\n")
newfile.write("Drosophila_simulans\n")
newfile.write(dsimseq + "\n")
newfile.write("Drosophila_virilis\n")
newfile.write(dvirseq + "\n")
newfile.write("Drosophila_willistoni\n")
newfile.write(dwilseq + "\n")
newfile.write("Drosophila_yakuba\n")
newfile.write(dyakseq)
newfile.close()



