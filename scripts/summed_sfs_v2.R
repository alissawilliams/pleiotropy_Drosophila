# summed_sfs.R
# script to take SFS files for each gene in each class and sum them into a single SFS
# need to bootstrap by sampling genes with replacement in each class
# same as summed_sfs.R except now preserving gene IDs
# June 20, 2022

library(stringr)

# get into directory with the tables of compiled sfs
setwd("~/Desktop/pleiotropy_Dmelanogaster/MK_analyses/multiDFE_sum/ZI/")

## RAL ##

# read in tables
nonsyntable = read.table("all_devo_nonsyn_SFS_ZI.txt", sep=" ", fill=TRUE) # fill=TRUE allows rows with NA to be read
syntable = read.table("all_devo_syn_SFS_ZI.txt", sep=" ", fill=TRUE) # fill=TRUE allows rows with NA to be read
geneidtable = read.table("all_devo_geneIDs_SFS_ZI.txt", col.names = c("geneid"))

#write.table(nonsyntable, "check_NAs_nonsyn.txt")

# get rid of rows with NAs in all three tables
# save indices with NAs into list and then delete those indices
indexlist = c()
for (i in 1:nrow(nonsyntable)){
  if (toString(nonsyntable[i,2]) == "NA"){
    indexlist = append(indexlist, i)
  }
}
# delete using subsetting
nonsyntable = nonsyntable[-indexlist,]
syntable = syntable[-indexlist,]
geneidtable = geneidtable[-indexlist,]

nrow(nonsyntable) == nrow(syntable) # make sure these match
nrow(syntable) == length(geneidtable)

setwd("~/Desktop/pleiotropy_Dmelanogaster/MK_analyses/multiDFE_sum/ZI/devo/")

# now make 100 tables by bootstrapping and save each to a file
# also save the gene IDs that go into each file and name those files with the replicate number
for (i in 1:100){
  newtablenonsyn = data.frame()
  newtablesyn = data.frame()
  newids = data.frame()
  for (j in 1:nrow(nonsyntable)){
    rownum = sample(1:nrow(nonsyntable),1) # randomly select a row index
    newtablenonsyn = rbind(newtablenonsyn, nonsyntable[rownum,])
    newtablesyn = rbind(newtablesyn, syntable[rownum,])
    newids = append(newids, geneidtable[rownum])
  }
  filename = paste("devo_ZI_bootstrap_", toString(i), ".sfs", sep="")
  genefilename = paste("devo_ZI_bootstrap_", toString(i), ".geneids.txt", sep="")
  write(154, file = filename, append = FALSE) # sample size on first line
  nonsynsums = colSums(newtablenonsyn)
  nonsynsums = toString(nonsynsums)
  nonsynsums = str_replace_all(nonsynsums, ",", "") 
  synsums = colSums(newtablesyn)
  synsums = toString(synsums)
  synsums = str_replace_all(synsums, ",", "")
  write(nonsynsums, file = filename, append = TRUE)
  write(synsums, file = filename, append = TRUE)
  for (entry in newids){
    write(entry, file=genefilename, append=TRUE)
  }
}



