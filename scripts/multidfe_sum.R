# multidfe_sum.R
# script to calculate alpha and omega_a with the bootstrapped values
# Alissa Williams
# June 20, 2022

library(stringr)
library(dunn.test)

# define Jukes-Cantor function
# from https://github.com/kousathanas/MultiDFE
# ***div.jukes***
# calculates Jukes-Cantor divergence.
# Input: x<-total sites,y<-site diffs
div.jukes<-function(x,y)
{
  d<-vector(length=length(x));
  for (i in 1:length(x))
  {
    if (y[i]<=0){d[i]=NA;next;}
    p=y[i]/x[i]
    if ((1-(4/3)*p)<0){d[i]=NA;next;}
    d[i]=(-3/4)*log(1-(4/3)*p)
  }
  
  return(d)
}

setwd("~/Desktop/pleiotropy_Dmelanogaster/MK_analyses/multiDFE_sum/RAL/")
setwd("~/Desktop/pleiotropy_Dmelanogaster/MK_analyses/multiDFE_sum/ZI/")

# read in PopFlyData
library(iMKT)
loadPopFly()
popral = subset(PopFlyData, Pop == "RAL")
popzi = subset(PopFlyData, Pop == "ZI")

# read in list of MultiDFE-outputted probabilities -- RAL
probspleiral = read.table("plei_fixation_multiDFE_RAL_lognormal_sum.txt")
colnames(probspleiral) = c("GeneID", "fixprob")
probsnonpleiral = read.table("nonplei_fixation_multiDFE_RAL_lognormal_sum.txt")
colnames(probsnonpleiral) = c("GeneID", "fixprob")
probsdevoral = read.table("devo_fixation_multiDFE_RAL_lognormal_sum.txt")
colnames(probsdevoral) = c("GeneID", "fixprob")

probspleiral$class = "plei"
probsnonpleiral$class = "nonplei"
probsdevoral$class = "devo"

# read in list of MultiDFE-outputted probabilities -- ZI
probspleizi = read.table("plei_fixation_multiDFE_ZI_lognormal_sum.txt")
colnames(probspleizi) = c("GeneID", "fixprob")
probsnonpleizi = read.table("nonplei_fixation_multiDFE_ZI_lognormal_sum.txt")
colnames(probsnonpleizi) = c("GeneID", "fixprob")
probsdevozi = read.table("devo_fixation_multiDFE_ZI_lognormal_sum.txt")
colnames(probsdevozi) = c("GeneID", "fixprob")

probspleizi$class = "plei"
probsnonpleizi$class = "nonplei"
probsdevozi$class = "devo"

#probs = rbind(probspleiral, probsnonpleiral, probsdevoral)
probs = rbind(probspleizi, probsnonpleizi, probsdevozi)

# make columns for new values
# initiate as numeric so I don't have to deal with converting later
probs$pi = 0 # from popzi
probs$p0 = 0 # from popzi
probs$di = 0 # from popzi
probs$d0 = 0 # from popzi
probs$mi = 0 # from popzi
probs$m0 = 0 # from popzi
probs$alpha = 0 # calculated
probs$omegaA = 0 # calculated
# add in columns for corrected data
probs$dicorr = 0
probs$d0corr = 0
probs$alphacorr = 0
probs$omegaAcorr = 0

# do corrections on RAL population data. will need to extract mi and m0 from PopFlyData subsets. 
# correction from MultiDFE GitHub page
# need to get pi, p0, di, d0, mi, and m0 from sums of component genes. will have to loop through. 
for (i in 1:nrow(probs)){
  bootstrapnum = probs[i,1] # get name (minus extension) of file
  geneidfile = paste(toString(bootstrapnum), ".geneids.txt", sep="")
  geneinfo = read.table(geneidfile) # read in file containing component genes
  geneinfo$pi = 0 # from popzi
  geneinfo$p0 = 0 # from popzi
  geneinfo$di = 0 # from popzi
  geneinfo$d0 = 0 # from popzi
  geneinfo$mi = 0 # from popzi
  geneinfo$m0 = 0 # from popzi
  for (j in 1:nrow(geneinfo)){
    genename = geneinfo[j,1]
    rowmatch = match(genename, popzi$Name)
    geneinfo[j,2] = popzi[rowmatch, 6] # add entries to geneinfo table
    geneinfo[j,3] = popzi[rowmatch, 5]
    geneinfo[j,4] = popzi[rowmatch,7]
    geneinfo[j,5] = popzi[rowmatch,8]
    geneinfo[j,6] = popzi[rowmatch, 10]
    geneinfo[j,7] = popzi[rowmatch, 11]
  }
  pi = sum(geneinfo$pi)
  p0 = sum(geneinfo$p0)
  di = sum(geneinfo$di)
  d0 = sum(geneinfo$d0)
  mi = sum(geneinfo$mi)
  m0 = sum(geneinfo$m0)
  fixprob = probs[i, 2]
  probs[i,4] = pi
  probs[i,5] = p0
  probs[i,6] = di
  probs[i,7] = d0
  probs[i,8] = mi
  probs[i,9] = m0
  probs[i,10] = (di - (d0 * fixprob))/di # uncorrected alpha calculation
  probs[i,11] = (di - (d0 * fixprob))/d0 # uncorrected omega_a calculation
  dcorr = div.jukes(c(mi, m0), c(di, d0)) # calculate both dicorr and d0corr at once
  probs[i, 12] = dcorr[1] # add dicorr
  probs[i, 13] = dcorr[2] # add d0corr
  probs[i,14] = (dcorr[1] - (dcorr[2] * fixprob))/dcorr[1] # alpha calculation
  probs[i,15] = (dcorr[1] - (dcorr[2] * fixprob))/dcorr[2] # omega_a calculation
}

#write.table(probs, "all_values_RAL_lognormal_sum_plei.txt", quote = FALSE, row.names = FALSE)
#write.table(probs, "all_values_RAL_lognormal_sum_plei_nonplei.txt", quote = FALSE, row.names = FALSE)
#write.table(probs, "all_values_RAL_lognormal_sum_plei_three_classes.txt", quote = FALSE, row.names = FALSE)
write.table(probs, "all_values_ZI_lognormal_sum_plei_three_classes.txt", quote = FALSE, row.names = FALSE)

pdf("boxplot_all_categories_ZI_alpha.pdf")
boxplot(probs$alphacorr~probs$class)
dev.off()

kruskal.test(alphacorr ~ class, data = probs) # p-value < 2.2e-16 for RAL and ZI

dunn.test(probs$alphacorr, probs$class, method="bh")

# omega_a
pdf("boxplot_all_categories_ZI_omegaA.pdf")
boxplot(probs$omegaAcorr~probs$class)
dev.off()

kruskal.test(omegaAcorr ~ class, data = probs) # p-value < 2.2e-16 for ZI
dunn.test(probs$omegaAcorr, probs$class, method="bh")


