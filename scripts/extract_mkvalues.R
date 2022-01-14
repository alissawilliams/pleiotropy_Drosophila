# extract_mkvalues.R
# script to read in File S3 from Fraisse et al, 2017 and and extract entries for genes of interest
# Alissa Williams
# January 11, 2022

# read in table of calculated MK values
setwd("/Users/alissawilliams/Desktop/pleiotropy_Dmelanogaster/MK_analyses")
mktable = read.table("Fraisse_etal_2017_FileS3.txt", header = TRUE)

# read in lists of genes of interest
pleigenes = read.table("plei_list.txt")
nonpleigenes = read.table("nonplei_list.txt")
devogenes = read.table("devo_list.txt")

### pleiotropic genes ###

# make table of MK values for pleiotropic genes
# also keep track of which genes didn't make the Fraisse et al 2017 list
pleimissing = list() # make list of genes that aren't in table
pleimk = data.frame() # make table for genes that are in the table
j = 1 # accumulator to remember what row of new table we're on
for (i in 1:nrow(pleigenes)){
  gene = pleigenes[i,1]
  rownum = which(mktable$geneId==gene)
  if (length(rownum) == 0){ # if the gene doesn't exist in mktable
    pleimissing = append(pleimissing, gene)
  } else{ # if the gene does exist in mktable
    pleimk[j,1] = gene # gene name
    pleimk[j,2] = mktable[rownum,6] # Ps
    pleimk[j,3] = mktable[rownum,7] # Pn
    pleimk[j,4] = mktable[rownum,8] # Ds
    pleimk[j,5] = mktable[rownum,9] # Dn
    j = j + 1
  }
}
colnames(pleimk) = c("geneId", "Ps", "Pn", "Ds", "Dn")

# write missing genes to a file
lapply(pleimissing, write, "plei_missing_genes_MK_table.txt", append=TRUE)

# write MK values to another file 
write.table(pleimk, file = "plei_genes_mk_vals.txt", quote = FALSE, row.names = FALSE, col.names = TRUE)


### nonpleiotropic genes ###

# make table of MK values for nonpleiotropic genes
# also keep track of which genes didn't make the Fraisse et al 2017 list
nonpleimissing = list() # make list of genes that aren't in table
nonpleimk = data.frame() # make table for genes that are in the table
j = 1 # accumulator to remember what row of new table we're on
for (i in 1:nrow(nonpleigenes)){
  gene = nonpleigenes[i,1]
  rownum = which(mktable$geneId==gene)
  if (length(rownum) == 0){ # if the gene doesn't exist in mktable
    nonpleimissing = append(nonpleimissing, gene)
  } else{ # if the gene does exist in mktable
    nonpleimk[j,1] = gene # gene name
    nonpleimk[j,2] = mktable[rownum,6] # Ps
    nonpleimk[j,3] = mktable[rownum,7] # Pn
    nonpleimk[j,4] = mktable[rownum,8] # Ds
    nonpleimk[j,5] = mktable[rownum,9] # Dn
    j = j + 1
  }
}
colnames(nonpleimk) = c("geneId", "Ps", "Pn", "Ds", "Dn")

# write missing genes to a file
lapply(nonpleimissing, write, "nonplei_missing_genes_MK_table.txt", append=TRUE)

# write MK values to another file 
write.table(nonpleimk, file = "nonplei_genes_mk_vals.txt", quote = FALSE, row.names = FALSE, col.names = TRUE)


### developmental genes ###

# make table of MK values for devo genes
# also keep track of which genes didn't make the Fraisse et al 2017 list
devomissing = list() # make list of genes that aren't in table
devomk = data.frame() # make table for genes that are in the table
j = 1 # accumulator to remember what row of new table we're on
for (i in 1:nrow(devogenes)){
  gene = devogenes[i,1]
  rownum = which(mktable$geneId==gene)
  if (length(rownum) == 0){ # if the gene doesn't exist in mktable
    devomissing = append(devomissing, gene)
  } else{ # if the gene does exist in mktable
    devomk[j,1] = gene # gene name
    devomk[j,2] = mktable[rownum,6] # Ps
    devomk[j,3] = mktable[rownum,7] # Pn
    devomk[j,4] = mktable[rownum,8] # Ds
    devomk[j,5] = mktable[rownum,9] # Dn
    j = j + 1
  }
}
colnames(devomk) = c("geneId", "Ps", "Pn", "Ds", "Dn")

# write missing genes to a file
lapply(devomissing, write, "devo_missing_genes_MK_table.txt", append=TRUE)

# write MK values to another file 
write.table(devomk, file = "devo_genes_mk_vals.txt", quote = FALSE, row.names = FALSE, col.names = TRUE)

