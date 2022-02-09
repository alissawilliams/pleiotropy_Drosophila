Abbreviations:
plei = pleiotropic genes
nonplei/nonpleiotropic = non-pleiotropic immune genes
devo/developmental = non-pleiotropic developmental genes

Note: each of the categories above is referred to as a gene class, gene category, class, or category. 

CDS_sequences.zip:
Contains three folders: seqfiles_developmental_genes_edited, seqfiles_nonpleiotropic_genes_edited, and seqfiles_pleiotropic_genes_edited. The folder structure in each of these folders is:
- not_enough_seqs contains CDSs for genes that had 0 or 1 sequences for the 12 Drosophila species (after removal of species with paralogs)
- originals contains unaligned, untrimmed CDSs for all genes with at least 2 sequences for the 12 Drosophila species (where each represented species only has one sequence; species with paralogs were removed)
- trimmed contains the final sequence files used in concatenations and individual gene runs. Within trimmed is individual_trees, which contains the .nwk format trees used to run codeml for each individual gene. 
- trimmed_originals contains the final sequence files (same as above) but with the original gene IDs instead of just species names like the ones above.

codeml_output_individual_genes.zip:
Contains model 0 output (model = 0, NSsites = 0) for each individual gene, i.e. where each gene is assigned one dN/dS value for the entire tree. The genes are separated into their categories in the folders devo_codeml_output, nonplei_codeml_output, and plei_codeml_output. In each of those respective folders, you'll find:
- a bunch of files in the format aligned_edited_FBgnxxxxxxx.model0.site.result.txt. These are the codeml output files. 
- grepfile.txt: has results of grep command used to pull out omega value from each file
- [category]_dnds_values.txt: table with two columns, gene ID and omega value for that gene
- [category]_nodnds_values.txt: list of genes for which this codeml run did not produce an omega value. 

codeml_output_individual_genes_models7and8.zip:
Contains model 0 output (model = 0, NSsites = 0), model 7 output (model = 0, NSsites = 7), and model 8 output (model = 0, NSsites = 8) for each individual pleiotropic gene. Note that only pleiotropic genes are included. Also note that for consistency, model 0 estimates for individual genes were taken from the files in codeml_output_individual_genes.zip, NOT from these combined runs.

individual_genes_fulltable_codeml_model0.txt: 
full table of codeml model 0 results for all individual genes. Made using the [category]_dnds_values.txt tables described above. 

sequence_counts.xlsx:
The first tab shows the number of sequences we started with at the beginning (from Table 1, row 2 in the manuscript). The first sheet then provides data on how many genes remained in each group after removing genes with too few sequences (which happened after removing species with gene duplicates) and then removing genes whose sequence files didn't align. Finally, of those sequence files that aligned, a number is also shown to represent the number of those genes for which NSsites = 0 codeml runs were successful. The numbers under "Sequence files that aligned" represent the concatenations, while the numbers under "Number of genes where model 0 run was successful" represent genes used in the distributions of individual NSsites = 0 dN/dS values. 
The second tab shows the number of genes found in the two relevant Fraisse et al 2017 files (after starting with the lists of genes that made it into the three concatenations for PAML). 

TollIMDJakSTAT_omegas_updated.xlsx:
Contains data for pleiotropic and immune non-pleiotropic genes of interest from codeml site models M0, M7, and M8. Models 7 and 8 are compared using their log likelihood scores (lnLs) in the equation 2*(lnL8 - lnL7). The result of that equation is a test statistic approximated by a chi square distribution, so this file also contains a p-value from a chi square distribution (the built in function in Excel) with df = 2. For negative test statistics, the p-value is 1. M7 creates 10 classes of sites, each representing 10% of the sites in the alignment (in this case, codons), where each class is constrained at a dN/dS value (omega) less than 1. M8 creates 11 classes of sites where each class is of variable proportion and, like M7, has its own omega value. The 11th class of sites is constrained to have an omega value of at least 1. The comparison of M8 vs M7 tells us whether a model containing a class with dN/dS >= 1 is a significantly better fit to the data than a model with all dN/dS values < 1. 

In concatenations/:

codeml_plei_model0.ctl and codeml_plei_models7and8.ctl: examples of control files used in PAML codeml for concatenations

Drosophila_species_tree.nwk: known species tree of all 12 Drosophila species on FlyBase. Used as the constraint tree in the PAML runs on concatenated alignments. Also used as the basis for constructing trees for each individual gene (see CDS_sequences.zip above). 

[class]_list_concatenation.txt:
Lists of the genes in each category that ended up being included in each respective concatenation. 

Then there are three folders: devo, nonplei, and plei. In each:
- concat_[class]_genes_noG.fas: concatenated alignment used in PAML codeml run
- concat_[class]_genes_paml_noG_NSsites0.out: output of model 0 run (model = 0, NSsites = 0)
- concat_[class]_genes_paml_noG.out: output of model 7 and model 8, which were performed using the same run (model = 0, NSsites = 7 8)
- the devo concatenation was large enough that NSsites7 and NSsites8 are in separate output files (named with same convention as above)

In McDonald-Kreitman/:

[class]_genes_mk_vals.txt:
Modified version of File S5 from Fraisse et al, 2017 that includes only the genes that were included in that particular class's concatenation (note that not all genes in the concatenation were found in these tables; see below). 

[class]_missing_genes_MK_table.txt:
List of genes from particular class concatenation that were not found in File S5 from Fraisse et al, 2017. 

fullMKtable.txt:
Full table of MK data from File S5 (Fraisse et al, 2017) for all genes of interest found in the concatenation and File S5. MAde using the [class]_genes_mk_table.txt table described above.

In scripts/:

concatenate.py:
Script to prepare fasta files for PAML
Uses a folder containing fasta files to be concatenated for use in PAML with option G for codon sequences (codeml with seqtype = 1). Hardcoded for specific folders and header format. Could be modified for different file formats. 

construct_tree.R:
Script to construct trees for PAML
Uses the original species tree and drops tips not found in the fasta sequence file for use in codeml runs for individual genes. Hardcoded file names. 

eliminate_dups.py:
Script to remove species with >1 sequence
Uses table created by one_to_one.R to read through fasta files and eliminate species with more than one sequence. Assumes that species with more than one sequence only have one sequence in the fasta file. File names are hardcoded. Could be modified for different formats.

extract_mkvalues.R:
Script for extracting values for MK tests
Obtains values for McDonald-Kreitman tests. Uses File S3 from Fraisse et al, 2017 and lists of genes of interest to output 1) a list of genes of interest missing in Table S3 and 2) a table of values for the genes of interest found in File S3. Again, file names are hard coded. An almost identical version of this script was used to extract entire table rows for genes of interest from File S5 (also Fraisse et al, 2017).

extract_seqs4.py:
Script for constructing original sequence files
Uses downloaded fasta sequences from FlyBase for each species of interest and a table of ortholog gene IDs (also from FlyBase) to construct sequence files. Also requires a list (text file) of genes of interest. Could be modified for different file formats. Currently, file names are hard coded.

gene_list.py:
Script to extract relevant columns from table
Uses a list of genes of interest and an ortholog table (from FlyBase) to create a version of the table only containing genes of interest.

num_seqs.py:
Script to remove sequence files with <2 sequences
Reads in fasta files and moves any files with fewer than 2 sequences to a different folder.

one_to_one.R:
Script for determining copy number of genes
Uses (modified) table of orthologs from FlyBase plus a list of genes of interest to determine which of those genes have one-to-one orthologs across all species of interest. File names are hardcoded. Could be modified for different files/formats.