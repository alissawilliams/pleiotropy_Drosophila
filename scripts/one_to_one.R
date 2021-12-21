# one_to_one.R
# script to determine which genes in 
# dmel_orthologs_in_drosophila_species_fb_2020_02_geneListOnly_extraction.tsv 
# are actually present in just one copy per species 
# Alissa Williams
# December 1, 2021

setwd("/Users/alissawilliams/Desktop/pleiotropy_Dmelanogaster/compiling_CDS/")

# read in list of genes of interest
#genes = read.table("all_Dmel_genes.txt")
genes = read.table("./ID_lists/nonpleiotropic_immune_genes_list.txt") 
#genes = read.table("./ID_lists/pleiotropic_immune_genes_list.txt") 

# read in ortholog list
orthos = read.table("dmel_orthologs_in_drosophila_species_fb_2020_02_geneListOnly_extraction.tsv", col.names = c("Dmel_ID","other_ID","other_species"))

# loop through each gene of interest and see which ones are truly one-to-one across all species
counttable = data.frame(matrix(nrow = nrow(genes), ncol = 12))
colnames(counttable) = c("Dmel_ID","dana","dere","dgri","dmoj","dper","dpse","dsec","dsim","dvir","dwil","dyak")
for (i in 1:nrow(genes)){
  # pull out gene ID
  id = genes[i,1] 
  # subset orthos table for that gene ID
  table = subset(orthos, Dmel_ID == id)
  # figure out how many times each species is represented
  danacount = nrow(subset(table, other_species == "Dana"))
  derecount = nrow(subset(table, other_species == "Dere"))
  dgricount = nrow(subset(table, other_species == "Dgri"))
  dmojcount = nrow(subset(table, other_species == "Dmoj"))
  dpercount = nrow(subset(table, other_species == "Dper"))
  dpsecount = nrow(subset(table, other_species == "Dpse"))
  dseccount = nrow(subset(table, other_species == "Dsec"))
  dsimcount = nrow(subset(table, other_species == "Dsim"))
  dvircount = nrow(subset(table, other_species == "Dvir"))
  dwilcount = nrow(subset(table, other_species == "Dwil"))
  dyakcount = nrow(subset(table, other_species == "Dyak"))
  # if any of the numbers are >1, write to file of duplicated genes
  # else, write to file of single-copy genes
  if (danacount > 1 | derecount > 1 | dgricount > 1 | dmojcount > 1 | dpercount > 1 | dpsecount > 1 | dseccount > 1 | dsimcount > 1 | dvircount > 1 | dwilcount > 1 | dyakcount > 1){
    write(id, file = "nonpleiduplicated_genes.txt", append = TRUE)
  } else {
    write(id, file = "nonpleisingle_copy_genes.txt", append = TRUE)
  }
  counttable[i,] = c(id, danacount, derecount, dgricount, dmojcount, dpercount, dpsecount, dseccount, dsimcount, dvircount, dwilcount, dyakcount)
}

#write.csv(counttable, file = "plei_copy_number_counts.csv", quote = FALSE, row.names = FALSE)
write.csv(counttable, file = "nonplei_copy_number_counts.csv", quote = FALSE, row.names = FALSE)

# accumulator to count number of genes where every non-Dmel species has a duplicate
dups = 0
for (i in 1:nrow(genes)){
  # pull out gene ID
  id = genes[i,1] 
  # subset orthos table for that gene ID
  table = subset(orthos, Dmel_ID == id)
  # accumulator for number of species with more than 1 copy and also not 0 copies
  greaterthan1and0 = 0
  # figure out how many times each species is represented
  danacount = nrow(subset(table, other_species == "Dana"))
  derecount = nrow(subset(table, other_species == "Dere"))
  dgricount = nrow(subset(table, other_species == "Dgri"))
  dmojcount = nrow(subset(table, other_species == "Dmoj"))
  dpercount = nrow(subset(table, other_species == "Dper"))
  dpsecount = nrow(subset(table, other_species == "Dpse"))
  dseccount = nrow(subset(table, other_species == "Dsec"))
  dsimcount = nrow(subset(table, other_species == "Dsim"))
  dvircount = nrow(subset(table, other_species == "Dvir"))
  dwilcount = nrow(subset(table, other_species == "Dwil"))
  dyakcount = nrow(subset(table, other_species == "Dyak"))
  if (danacount > 1 & derecount > 1 & dgricount > 1 & dmojcount > 1 & dpercount > 1 & dpsecount > 1 & dseccount > 1 & dsimcount > 1 & dvircount > 1 & dwilcount > 1 & dyakcount > 1){
    dups = dups + 1
  }
  
}
print(dups)




