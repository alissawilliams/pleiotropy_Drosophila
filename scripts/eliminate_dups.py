#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 11:33:50 2021

@author: alissawilliams
"""

import os
from Bio import SeqIO

os.chdir("/Users/alissawilliams/Desktop/pleiotropy_Dmelanogaster/compiling_CDS/")

# read in table of counts and make a dictionary
#countsfile = open("plei_copy_number_counts.csv","r")
#countsfile = open("nonplei_copy_number_counts.csv","r")
countsfile = open("./devo_genes/devo_copy_number_counts.csv","r")
# initiate dictionary
countsdict = {}
for line in countsfile:
    linesplit = line.split(",")
    countsdict[linesplit[0]+"_Dana"] = linesplit[1]
    countsdict[linesplit[0]+"_Dere"] = linesplit[2]
    countsdict[linesplit[0]+"_Dgri"] = linesplit[3]
    countsdict[linesplit[0]+"_Dmoj"] = linesplit[4]
    countsdict[linesplit[0]+"_Dper"] = linesplit[5]
    countsdict[linesplit[0]+"_Dpse"] = linesplit[6]
    countsdict[linesplit[0]+"_Dsec"] = linesplit[7]
    countsdict[linesplit[0]+"_Dsim"] = linesplit[8]
    countsdict[linesplit[0]+"_Dvir"] = linesplit[9]
    countsdict[linesplit[0]+"_Dwil"] = linesplit[10]
    countsdict[linesplit[0]+"_Dyak"] = linesplit[11].strip() # get rid of newline on last entry

countsfile.close()

# now iterate through files in directory 
#for filename in os.listdir("seqfiles_pleiotropic_genes"):
#for filename in os.listdir("seqfiles_nonpleiotropic_genes"):
for filename in os.listdir("seqfiles_developmental_genes"):
    # if the file is a fasta file (to avoid the hidden files)
    if filename.endswith(".fasta"):
        genename = filename.split(".")[0]
        #seqdict = SeqIO.to_dict(SeqIO.parse("./seqfiles_pleiotropic_genes/"+filename, "fasta"))
        #newfilename = "./seqfiles_pleiotropic_genes_edited/" + "edited_" + filename
        #seqdict = SeqIO.to_dict(SeqIO.parse("./seqfiles_nonpleiotropic_genes/"+filename, "fasta"))
        #newfilename = "./seqfiles_nonpleiotropic_genes_edited/" + "edited_" + filename
        seqdict = SeqIO.to_dict(SeqIO.parse("./seqfiles_developmental_genes/"+filename, "fasta"))
        newfilename = "./seqfiles_developmental_genes_edited/" + "edited_" + filename
        newfile = open(newfilename, "w")
        # check whether Dmel sequence is not empty, and if so add it to the edited file
        searchkey = "Dmel"
        res = [val for key, val in seqdict.items() if searchkey in key]
        resid = str(res).split(",")[2]
        resid = resid.split("=")[1]
        resid = resid.split("'")[1]
        if str(seqdict[resid].seq) != "":
            newfile.write(">" + resid + "\n")
            newfile.write(str(seqdict[resid].seq) + "\n")
        # check whether each species is single copy, and if so add it to the edited file
        if int(countsdict[filename.split(".")[0] + "_Dana"]) == 1:
            searchkey = "Dana"
            # get key that contains "Dana"
            res = [val for key, val in seqdict.items() if searchkey in key]
            resid = str(res).split(",")[2]
            resid = resid.split("=")[1]
            resid = resid.split("'")[1]
            newfile.write(">" + resid + "\n")
            newfile.write(str(seqdict[resid].seq) + "\n")
        if int(countsdict[filename.split(".")[0] + "_Dere"]) == 1:
            searchkey = "Dere"
            # get key that contains "Dana"
            res = [val for key, val in seqdict.items() if searchkey in key]
            resid = str(res).split(",")[2]
            resid = resid.split("=")[1]
            resid = resid.split("'")[1]
            newfile.write(">" + resid + "\n")
            newfile.write(str(seqdict[resid].seq) + "\n")
        if int(countsdict[filename.split(".")[0] + "_Dgri"]) == 1:
            searchkey = "Dgri"
            # get key that contains "Dana"
            res = [val for key, val in seqdict.items() if searchkey in key]
            resid = str(res).split(",")[2]
            resid = resid.split("=")[1]
            resid = resid.split("'")[1]
            newfile.write(">" + resid + "\n")
            newfile.write(str(seqdict[resid].seq) + "\n")
        if int(countsdict[filename.split(".")[0] + "_Dmoj"]) == 1:
            searchkey = "Dmoj"
            # get key that contains "Dana"
            res = [val for key, val in seqdict.items() if searchkey in key]
            resid = str(res).split(",")[2]
            resid = resid.split("=")[1]
            resid = resid.split("'")[1]
            newfile.write(">" + resid + "\n")
            newfile.write(str(seqdict[resid].seq) + "\n")
        if int(countsdict[filename.split(".")[0] + "_Dper"]) == 1:
            searchkey = "Dper"
            # get key that contains "Dana"
            res = [val for key, val in seqdict.items() if searchkey in key]
            resid = str(res).split(",")[2]
            resid = resid.split("=")[1]
            resid = resid.split("'")[1]
            newfile.write(">" + resid + "\n")
            newfile.write(str(seqdict[resid].seq) + "\n")
        if int(countsdict[filename.split(".")[0] + "_Dpse"]) == 1:
            searchkey = "Dpse"
            # get key that contains "Dana"
            res = [val for key, val in seqdict.items() if searchkey in key]
            resid = str(res).split(",")[2]
            resid = resid.split("=")[1]
            resid = resid.split("'")[1]
            newfile.write(">" + resid + "\n")
            newfile.write(str(seqdict[resid].seq) + "\n")
        if int(countsdict[filename.split(".")[0] + "_Dsec"]) == 1:
            searchkey = "Dsec"
            # get key that contains "Dana"
            res = [val for key, val in seqdict.items() if searchkey in key]
            resid = str(res).split(",")[2]
            resid = resid.split("=")[1]
            resid = resid.split("'")[1]
            newfile.write(">" + resid + "\n")
            newfile.write(str(seqdict[resid].seq) + "\n")
        if int(countsdict[filename.split(".")[0] + "_Dsim"]) == 1:
            searchkey = "Dsim"
            # get key that contains "Dana"
            res = [val for key, val in seqdict.items() if searchkey in key]
            resid = str(res).split(",")[2]
            resid = resid.split("=")[1]
            resid = resid.split("'")[1]
            newfile.write(">" + resid + "\n")
            newfile.write(str(seqdict[resid].seq) + "\n")
        if int(countsdict[filename.split(".")[0] + "_Dvir"]) == 1:
            searchkey = "Dvir"
            # get key that contains "Dana"
            res = [val for key, val in seqdict.items() if searchkey in key]
            resid = str(res).split(",")[2]
            resid = resid.split("=")[1]
            resid = resid.split("'")[1]
            newfile.write(">" + resid + "\n")
            newfile.write(str(seqdict[resid].seq) + "\n")
        if int(countsdict[filename.split(".")[0] + "_Dwil"]) == 1:
            searchkey = "Dwil"
            # get key that contains "Dana"
            res = [val for key, val in seqdict.items() if searchkey in key]
            resid = str(res).split(",")[2]
            resid = resid.split("=")[1]
            resid = resid.split("'")[1]
            newfile.write(">" + resid + "\n")
            newfile.write(str(seqdict[resid].seq) + "\n")
        if int(countsdict[filename.split(".")[0] + "_Dyak"]) == 1:
            searchkey = "Dyak"
            # get key that contains "Dana"
            res = [val for key, val in seqdict.items() if searchkey in key]
            resid = str(res).split(",")[2]
            resid = resid.split("=")[1]
            resid = resid.split("'")[1]
            newfile.write(">" + resid + "\n")
            newfile.write(str(seqdict[resid].seq) + "\n")
        newfile.close()
        

#searchkey = "Dana"
#res = [val for key, val in seqdict.items() if searchkey in key]






