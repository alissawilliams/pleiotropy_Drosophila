#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 23 14:51:17 2022

@author: alissawilliams

code adapted from https://nbviewer.org/github/jmurga/iMKTData/blob/master/notebooks/dmelProteins.ipynb#Extracting-mi-and-m0
"""

import numpy as np
import pandas as pd

path = "/Users/alissawilliams/Desktop/pleiotropy_Dmelanogaster/MK_analyses/multiDFE_round2/"

# read in files
raldmelSites = pd.read_csv(path + 'RALdsimDmelSites_noDiv.txt', sep='\t') #, header=None)
#raldmelSites.columns = ['id','CHROM','POS','div','rawDerivedAllele','type','pop','rawcount']
#raldmelSites = raldmelSites.drop('type',axis=1)
raldmelSites.head()

zidmelSites = pd.read_csv(path + 'ZIdsimDmelSites_noDiv.txt', sep='\t') #, header=None)
#zidmelSites = zidmelSites.drop('type',axis=1)
zidmelSites.head()


# RAL population

#daf = raldmelSites[['id','rawcount','type','pop']][raldmelSites['rawcount']!=0]
raldaf = raldmelSites[['id','rawcountp','type']][raldmelSites['rawcountp']!=0]

# make bins 
#ralbins = np.arange(0,161,1)
#rallabels =  np.arange(0,161,1)

#raldaf['categories'] = pd.cut(raldaf['rawcount'],bins=ralbins,labels=rallabels)
#raldaf['categories'] = pd.cut(raldaf['rawcount'],bins=ralbins)

# all numbers are whole numbers
ralbins = np.arange(0.5,161.5,1)
rallabels = np.arange(1,161,1)
raldaf['categories'] = pd.cut(raldaf['rawcountp'],bins=ralbins,labels=rallabels)

sfs = raldaf.groupby(['id','type','categories']).count().reset_index()
sfs['rawcountp'] = sfs['rawcountp'].fillna(0).astype(int)
sfs = sfs.groupby(['id','type'])['rawcountp'].apply(list).reset_index()
sfs = sfs.pivot_table(index=['id'], columns=['type'],values='rawcountp',aggfunc=lambda x:x).reset_index()
sfs['0fold'] = sfs['0fold'].apply(lambda x:';'.join(map(str,x)))
sfs['4fold'] = sfs['4fold'].apply(lambda x:';'.join(map(str,x)))

sfs.columns = ['id','daf0f','daf4f']

# commented out so I don't accidentally overwrite previous files
#sfs.to_csv(path+"RAL_sfs.csv", sep='\t',header=True,index=False)

sfs.to_csv(testfile, header=None, index=None, sep='\t', mode='a')


# ZI population

zidaf = zidmelSites[['id','rawcountp','type']][zidmelSites['rawcountp']!=0]

# make bins 

# all numbers are whole numbers
zibins = np.arange(0.5,155.5,1)
zilabels = np.arange(1,155,1)
zidaf['categories'] = pd.cut(zidaf['rawcountp'],bins=zibins,labels=zilabels)

sfs = zidaf.groupby(['id','type','categories']).count().reset_index()
sfs['rawcountp'] = sfs['rawcountp'].fillna(0).astype(int)
sfs = sfs.groupby(['id','type'])['rawcountp'].apply(list).reset_index()
sfs = sfs.pivot_table(index=['id'], columns=['type'],values='rawcountp',aggfunc=lambda x:x).reset_index()
sfs['0fold'] = sfs['0fold'].apply(lambda x:';'.join(map(str,x)))
sfs['4fold'] = sfs['4fold'].apply(lambda x:';'.join(map(str,x)))

sfs.columns = ['id','daf0f','daf4f']

#sfs.to_csv(path+"ZI_sfs.csv", sep='\t',header=True,index=False)












