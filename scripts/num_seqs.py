#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 16:37:08 2021

@author: alissawilliams
"""

import os
from Bio import SeqIO

os.chdir("/Users/alissawilliams/Desktop/pleiotropy_Dmelanogaster/compiling_CDS/")

for filename in os.listdir("seqfiles_pleiotropic_genes_edited"):
    if filename.endswith(".fasta"):
        seqdict = SeqIO.to_dict(SeqIO.parse("./seqfiles_pleiotropic_genes_edited/"+filename, "fasta"))
        if len(seqdict) < 2:
            command = "mv " + "./seqfiles_pleiotropic_genes_edited/" + filename + " ./seqfiles_pleiotropic_genes_edited/not_enough_seqs/"
            os.system(command)

for filename in os.listdir("seqfiles_nonpleiotropic_genes_edited"):
    if filename.endswith(".fasta"):
        seqdict = SeqIO.to_dict(SeqIO.parse("./seqfiles_nonpleiotropic_genes_edited/"+filename, "fasta"))
        if len(seqdict) < 2:
            command = "mv " + "./seqfiles_nonpleiotropic_genes_edited/" + filename + " ./seqfiles_nonpleiotropic_genes_edited/not_enough_seqs/"
            os.system(command)

for filename in os.listdir("seqfiles_developmental_genes_edited"):
    if filename.endswith(".fasta"):
        seqdict = SeqIO.to_dict(SeqIO.parse("./seqfiles_developmental_genes_edited/"+filename, "fasta"))
        if len(seqdict) < 2:
            command = "mv " + "./seqfiles_developmental_genes_edited/" + filename + " ./seqfiles_developmental_genes_edited/not_enough_seqs/"
            os.system(command)


#for filename in os.listdir("seqfiles_pleiotropic_genes_edited"):
#    command = "grep -c \">\" " + filename
#    count = os.system(command)
            