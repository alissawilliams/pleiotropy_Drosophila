concatenate.py:
Script to prepare fasta files for PAML
Uses a folder containing fasta files to be concatenated for use in PAML with option G for codon sequences (codeml with seqtype = 1). Hardcoded for specific folders and header format. Could be modified for different file formats. 

eliminate_dups.py:
Script to remove species with >1 sequence
Uses table created by one_to_one.R to read through fasta files and eliminate species with more than one sequence. Assumes that species with more than one sequence only have one sequence in the fasta file. File names are hardcoded. Could be modified for different formats.

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