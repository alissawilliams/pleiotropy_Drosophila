# construct_tree.R
# script to read in a tree and sequence file and drop any species not represented in the sequence file
# Alissa Williams
# January 21, 2022

library(ape)
library(seqinr)

# read in tree file
fulltree = read.tree("/Users/alissawilliams/Desktop/pleiotropy_Dmelanogaster/paml/Drosophila_species_tree.nwk")

setwd("/Users/alissawilliams/Desktop/pleiotropy_Dmelanogaster/compiling_CDS/seqfiles_developmental_genes_edited/trimmed/")

# loop through all fasta files 
filenames = dir(pattern="*.fas")
for (file in filenames){
  seqs = read.fasta(file = file) # read fasta file
  headers = names(seqs) # get species names
  newtree = fulltree # make copy of main tree
  # remove tips from tree if species does not exist in fasta file (headers)
  if ("Drosophila_ananassae" %in% headers == FALSE){
    newtree = drop.tip(newtree, "Drosophila_ananassae")
  }
  if ("Drosophila_erecta" %in% headers == FALSE){
    newtree = drop.tip(newtree, "Drosophila_erecta")
  }
  if ("Drosophila_grimshawi" %in% headers == FALSE){
    newtree = drop.tip(newtree, "Drosophila_grimshawi")
  }
  if ("Drosophila_melanogaster" %in% headers == FALSE){
    newtree = drop.tip(newtree, "Drosophila_melanogaster")
  }
  if ("Drosophila_mojavensis" %in% headers == FALSE){
    newtree = drop.tip(newtree, "Drosophila_mojavensis")
  }
  if ("Drosophila_persimilis" %in% headers == FALSE){
    newtree = drop.tip(newtree, "Drosophila_persimilis")
  }
  if ("Drosophila_pseudoobscura" %in% headers == FALSE){
    newtree = drop.tip(newtree, "Drosophila_pseudoobscura")
  }
  if ("Drosophila_sechellia" %in% headers == FALSE){
    newtree = drop.tip(newtree, "Drosophila_sechellia")
  }
  if ("Drosophila_simulans" %in% headers == FALSE){
    newtree = drop.tip(newtree, "Drosophila_simulans")
  }
  if ("Drosophila_virilis" %in% headers == FALSE){
    newtree = drop.tip(newtree, "Drosophila_virilis")
  }
  if ("Drosophila_willistoni" %in% headers == FALSE){
    newtree = drop.tip(newtree, "Drosophila_willistoni")
  }
  if ("Drosophila_yakuba" %in% headers == FALSE){
    newtree = drop.tip(newtree, "Drosophila_yakuba")
  }
  write.tree(newtree, file = paste(file, ".nwk", sep = ""))
}







