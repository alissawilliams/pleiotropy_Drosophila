#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 16:49:13 2021

@author: alissawilliams
"""

import os
from Bio import SeqIO

os.chdir("/Users/alissawilliams/Desktop/pleiotropy_Dmelanogaster/compiling_CDS/")

# construct dictionary of key: Dmel ID + other species name, value: other species ID
allids = open("dmel_orthologs_in_drosophila_species_fb_2020_02_geneListOnly_extraction.tsv", "r")
drosdict = {}
for line in allids:
    linesplit = line.split()
    newkey = linesplit[0] + "_" + linesplit[2]
    # use only the first gene ID in the list in cases of paralogs
    if newkey not in drosdict.keys():
        drosdict[newkey] = linesplit[1]
    
    
# open the sequence files and make fasta dictionaries
# get sequence from first instance of that gene ID in the file

# Drosophila melanogaster pleiotropic genes
dmelpleidict = {}
for seq_record in SeqIO.parse("./fasta_files/Dmel_pleiotropic.fasta", "fasta"):
    des = seq_record.description
    dessplit = des.split(";")
    desparent = dessplit[6]
    desparent = desparent.strip()
    desparent = desparent.split(",")[0]
    desparent = desparent.split("=")[1]
    # if the key doesn't already exist in the dictionary
    if desparent not in dmelpleidict.keys():
        dmelpleidict[desparent] = str(seq_record.seq)
# this dictionary has fewer entries than genes...
    
# Drosophila melanogaster nonpleiotropic genes
dmelnonpleidict = {}
for seq_record in SeqIO.parse("./fasta_files/Dmel_nonpleiotropic.fasta", "fasta"):
    des = seq_record.description
    dessplit = des.split(";")
    desparent = dessplit[6]
    desparent = desparent.strip()
    desparent = desparent.split(",")[0]
    desparent = desparent.split("=")[1]
    # if the key doesn't already exist in the dictionary
    if desparent not in dmelnonpleidict.keys():
        dmelnonpleidict[desparent] = str(seq_record.seq)
# this one also has fewer entries than genes
    
# Drosophila erecta
deredict = {}
for seq_record in SeqIO.parse("./fasta_files/FlyBase_Dere.fasta", "fasta"):
    des = seq_record.description
    dessplit = des.split(";")
    desparent = dessplit[6]
    desparent = desparent.strip()
    desparent = desparent.split(",")[0]
    desparent = desparent.split("=")[1]
    # if the key doesn't already exist in the dictionary
    if desparent not in deredict.keys():
        deredict[desparent] = str(seq_record.seq)

# Drosophila sechellia
dsecdict = {}
for seq_record in SeqIO.parse("./fasta_files/FlyBase_Dsec.fasta", "fasta"):
    des = seq_record.description
    dessplit = des.split(";")
    desparent = dessplit[6]
    desparent = desparent.strip()
    desparent = desparent.split(",")[0]
    desparent = desparent.split("=")[1]
    # if the key doesn't already exist in the dictionary
    if desparent not in dsecdict.keys():
        dsecdict[desparent] = str(seq_record.seq)
    
# Drosophila simulans
dsimdict = {}
for seq_record in SeqIO.parse("./fasta_files/FlyBase_Dsim.fasta", "fasta"):
    des = seq_record.description
    dessplit = des.split(";")
    desparent = dessplit[6]
    desparent = desparent.strip()
    desparent = desparent.split(",")[0]
    desparent = desparent.split("=")[1]
    # if the key doesn't already exist in the dictionary
    if desparent not in dsimdict.keys():
        dsimdict[desparent] = str(seq_record.seq)

# Drosophila yakuba
dyakdict = {}
for seq_record in SeqIO.parse("./fasta_files/FlyBase_Dyak.fasta", "fasta"):
    des = seq_record.description
    dessplit = des.split(";")
    desparent = dessplit[6]
    desparent = desparent.strip()
    desparent = desparent.split(",")[0]
    desparent = desparent.split("=")[1]
    # if the key doesn't already exist in the dictionary
    if desparent not in dyakdict.keys():
        dyakdict[desparent] = str(seq_record.seq)

# new species

# Drosophila ananassae 
danadict = {}
for seq_record in SeqIO.parse("./fasta_files/FlyBase_Dana.fasta", "fasta"):
    des = seq_record.description
    dessplit = des.split(";")
    desparent = dessplit[6]
    desparent = desparent.strip()
    desparent = desparent.split(",")[0]
    desparent = desparent.split("=")[1]
    # if the key doesn't already exist in the dictionary
    if desparent not in danadict.keys():
        danadict[desparent] = str(seq_record.seq)

# Drosophila grimshawi 
dgridict = {}
for seq_record in SeqIO.parse("./fasta_files/FlyBase_Dgri.fasta", "fasta"):
    des = seq_record.description
    dessplit = des.split(";")
    desparent = dessplit[6]
    desparent = desparent.strip()
    desparent = desparent.split(",")[0]
    desparent = desparent.split("=")[1]
    # if the key doesn't already exist in the dictionary
    if desparent not in dgridict.keys():
        dgridict[desparent] = str(seq_record.seq)

# Drosophila mojavensis 
dmojdict = {}
for seq_record in SeqIO.parse("./fasta_files/FlyBase_Dmoj.fasta", "fasta"):
    des = seq_record.description
    dessplit = des.split(";")
    desparent = dessplit[6]
    desparent = desparent.strip()
    desparent = desparent.split(",")[0]
    desparent = desparent.split("=")[1]
    # if the key doesn't already exist in the dictionary
    if desparent not in dmojdict.keys():
        dmojdict[desparent] = str(seq_record.seq)

# Drosophila persimilis
dperdict = {}
for seq_record in SeqIO.parse("./fasta_files/FlyBase_Dper.fasta", "fasta"):
    des = seq_record.description
    dessplit = des.split(";")
    desparent = dessplit[6]
    desparent = desparent.strip()
    desparent = desparent.split(",")[0]
    desparent = desparent.split("=")[1]
    # if the key doesn't already exist in the dictionary
    if desparent not in dperdict.keys():
        dperdict[desparent] = str(seq_record.seq)

# Drosophila pseudoobscura
dpsedict = {}
for seq_record in SeqIO.parse("./fasta_files/FlyBase_Dpse.fasta", "fasta"):
    des = seq_record.description
    dessplit = des.split(";")
    desparent = dessplit[6]
    desparent = desparent.strip()
    desparent = desparent.split(",")[0]
    desparent = desparent.split("=")[1]
    # if the key doesn't already exist in the dictionary
    if desparent not in dpsedict.keys():
        dpsedict[desparent] = str(seq_record.seq)

# Drosophila virilis
dvirdict = {}
for seq_record in SeqIO.parse("./fasta_files/FlyBase_Dvir.fasta", "fasta"):
    des = seq_record.description
    dessplit = des.split(";")
    desparent = dessplit[6]
    desparent = desparent.strip()
    desparent = desparent.split(",")[0]
    desparent = desparent.split("=")[1]
    # if the key doesn't already exist in the dictionary
    if desparent not in dvirdict.keys():
        dvirdict[desparent] = str(seq_record.seq)

# Drosophila willistoni
dwildict = {}
for seq_record in SeqIO.parse("./fasta_files/FlyBase_Dwil.fasta", "fasta"):
    des = seq_record.description
    dessplit = des.split(";")
    desparent = dessplit[6]
    desparent = desparent.strip()
    desparent = desparent.split(",")[0]
    desparent = desparent.split("=")[1]
    # if the key doesn't already exist in the dictionary
    if desparent not in dwildict.keys():
        dwildict[desparent] = str(seq_record.seq)


# for pleiotropic gene list
pleigenes = open("./ID_lists/pleiotropic_immune_genes_list.txt", "r")

# construct a new fasta file for each gene ID in the pleigenes list
for line in pleigenes:
    line = line.strip()
    # make new file for sequence
    seqfilename = "/Users/alissawilliams/Desktop/pleiotropy_Dmelanogaster/compiling_CDS/seqfiles_pleiotropic_genes/" + line.strip() + ".fasta"
    seqfile = open(seqfilename, "w")
    # add Dmel sequence name and sequence if present
    seqfile.write(">" + "Dmel_" + line + "\n")
    if line in dmelpleidict.keys():
        seqfile.write(dmelpleidict[line] + "\n")
    # make key names for each non-Dmel sequence
    derekey = line + "_Dere"
    dseckey = line + "_Dsec"
    dsimkey = line + "_Dsim"
    dyakkey = line + "_Dyak"
    danakey = line + "_Dana"
    dgrikey = line + "_Dgri"
    dmojkey = line + "_Dmoj"
    dperkey = line + "_Dper"
    dpsekey = line + "_Dpse"
    dvirkey = line + "_Dvir"
    dwilkey = line + "_Dwil"
    # check whether each key is in dict, and if so, continue with extracting sequences
    if derekey in drosdict.keys():
        derevalue = drosdict[derekey]
        seqfile.write(">Dere_" + derevalue + "\n")
        if derevalue in deredict.keys():
            seqfile.write(deredict[derevalue] + "\n")
    if dseckey in drosdict.keys():
        dsecvalue = drosdict[dseckey]
        seqfile.write(">Dsec_" + dsecvalue + "\n")
        if dsecvalue in dsecdict.keys():
            seqfile.write(dsecdict[dsecvalue] + "\n")
    if dsimkey in drosdict.keys():
        dsimvalue = drosdict[dsimkey]
        seqfile.write(">Dsim_" + dsimvalue + "\n")
        if dsimvalue in dsimdict.keys():
            seqfile.write(dsimdict[dsimvalue] + "\n")
    if dyakkey in drosdict.keys():
        dyakvalue = drosdict[dyakkey]
        seqfile.write(">Dyak_" + dyakvalue + "\n")
        if dyakvalue in dyakdict.keys():
            seqfile.write(dyakdict[dyakvalue] + "\n")
    if danakey in drosdict.keys():
        danavalue = drosdict[danakey]
        seqfile.write(">Dana_" + danavalue + "\n")
        if danavalue in danadict.keys():
            seqfile.write(danadict[danavalue] + "\n")
    if dgrikey in drosdict.keys():
        dgrivalue = drosdict[dgrikey]
        seqfile.write(">Dgri_" + dgrivalue + "\n")
        if dgrivalue in dgridict.keys():
            seqfile.write(dgridict[dgrivalue] + "\n")
    if dmojkey in drosdict.keys():
        dmojvalue = drosdict[dmojkey]
        seqfile.write(">Dmoj_" + dmojvalue + "\n")
        if dmojvalue in dmojdict.keys():
            seqfile.write(dmojdict[dmojvalue] + "\n")
    if dperkey in drosdict.keys():
        dpervalue = drosdict[dperkey]
        seqfile.write(">Dper_" + dpervalue + "\n")
        if dpervalue in dperdict.keys():
            seqfile.write(dperdict[dpervalue] + "\n")
    if dpsekey in drosdict.keys():
        dpsevalue = drosdict[dpsekey]
        seqfile.write(">Dpse_" + dpsevalue + "\n")
        if dpsevalue in dpsedict.keys():
            seqfile.write(dpsedict[dpsevalue] + "\n")
    if dvirkey in drosdict.keys():
        dvirvalue = drosdict[dvirkey]
        seqfile.write(">Dvir_" + dvirvalue + "\n")
        if dvirvalue in dvirdict.keys():
            seqfile.write(dvirdict[dvirvalue] + "\n")
    if dwilkey in drosdict.keys():
        dwilvalue = drosdict[dwilkey]
        seqfile.write(">Dwil_" + dwilvalue + "\n")
        if dwilvalue in dwildict.keys():
            seqfile.write(dwildict[dwilvalue] + "\n")
    seqfile.close()


os.chdir("/Users/alissawilliams/Desktop/pleiotropy_Dmelanogaster/compiling_CDS/")
    
# for nonpleiotropic gene list
nonpleigenes = open("./ID_lists/nonpleiotropic_immune_genes_list.txt", "r")

# construct a new fasta file for each gene ID in the nonpleigenes list
for line in nonpleigenes:
    line = line.strip()
    # make new file for sequence
    seqfilename = "/Users/alissawilliams/Desktop/pleiotropy_Dmelanogaster/compiling_CDS/seqfiles_nonpleiotropic_genes/" + line + ".fasta"
    seqfile = open(seqfilename, "w")
    # add Dmel sequence name and sequence if present
    seqfile.write(">" + "Dmel_" + line + "\n")
    if line in dmelnonpleidict.keys():
        seqfile.write(dmelnonpleidict[line] + "\n")
    # make key names for each non-Dmel sequence
    derekey = line + "_Dere"
    dseckey = line + "_Dsec"
    dsimkey = line + "_Dsim"
    dyakkey = line + "_Dyak"
    danakey = line + "_Dana"
    dgrikey = line + "_Dgri"
    dmojkey = line + "_Dmoj"
    dperkey = line + "_Dper"
    dpsekey = line + "_Dpse"
    dvirkey = line + "_Dvir"
    dwilkey = line + "_Dwil"
    # check whether each key is in dict, and if so, continue with extracting sequences
    if derekey in drosdict.keys():
        derevalue = drosdict[derekey]
        seqfile.write(">Dere_" + derevalue + "\n")
        if derevalue in deredict.keys():
            seqfile.write(deredict[derevalue] + "\n")
    if dseckey in drosdict.keys():
        dsecvalue = drosdict[dseckey]
        seqfile.write(">Dsec_" + dsecvalue + "\n")
        if dsecvalue in dsecdict.keys():
            seqfile.write(dsecdict[dsecvalue] + "\n")
    if dsimkey in drosdict.keys():
        dsimvalue = drosdict[dsimkey]
        seqfile.write(">Dsim_" + dsimvalue + "\n")
        if dsimvalue in dsimdict.keys():
            seqfile.write(dsimdict[dsimvalue] + "\n")
    if dyakkey in drosdict.keys():
        dyakvalue = drosdict[dyakkey]
        seqfile.write(">Dyak_" + dyakvalue + "\n")
        if dyakvalue in dyakdict.keys():
            seqfile.write(dyakdict[dyakvalue] + "\n")
    if danakey in drosdict.keys():
        danavalue = drosdict[danakey]
        seqfile.write(">Dana_" + danavalue + "\n")
        if danavalue in danadict.keys():
            seqfile.write(danadict[danavalue] + "\n")
    if dgrikey in drosdict.keys():
        dgrivalue = drosdict[dgrikey]
        seqfile.write(">Dgri_" + dgrivalue + "\n")
        if dgrivalue in dgridict.keys():
            seqfile.write(dgridict[dgrivalue] + "\n")
    if dmojkey in drosdict.keys():
        dmojvalue = drosdict[dmojkey]
        seqfile.write(">Dmoj_" + dmojvalue + "\n")
        if dmojvalue in dmojdict.keys():
            seqfile.write(dmojdict[dmojvalue] + "\n")
    if dperkey in drosdict.keys():
        dpervalue = drosdict[dperkey]
        seqfile.write(">Dper_" + dpervalue + "\n")
        if dpervalue in dperdict.keys():
            seqfile.write(dperdict[dpervalue] + "\n")
    if dpsekey in drosdict.keys():
        dpsevalue = drosdict[dpsekey]
        seqfile.write(">Dpse_" + dpsevalue + "\n")
        if dpsevalue in dpsedict.keys():
            seqfile.write(dpsedict[dpsevalue] + "\n")
    if dvirkey in drosdict.keys():
        dvirvalue = drosdict[dvirkey]
        seqfile.write(">Dvir_" + dvirvalue + "\n")
        if dvirvalue in dvirdict.keys():
            seqfile.write(dvirdict[dvirvalue] + "\n")
    if dwilkey in drosdict.keys():
        dwilvalue = drosdict[dwilkey]
        seqfile.write(">Dwil_" + dwilvalue + "\n")
        if dwilvalue in dwildict.keys():
            seqfile.write(dwildict[dwilvalue] + "\n")
    seqfile.close()
