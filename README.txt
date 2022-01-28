Abbreviations:
plei = pleiotropic genes
nonplei/nonpleiotropic = non-pleiotropic immune genes
devo/developmental = non-pleiotropic developmental genes

CDS_sequences.zip:
Contains three folders: seqfiles_developmental_genes_edited, seqfiles_nonpleiotropic_genes_edited, and seqfiles_pleiotropic_genes_edited. The folder structure in each of these folders is:
- not_enough_seqs contains CDSs for genes that had 0 or 1 sequences for the 12 Drosophila species (after removal of species with paralogs)
- originals contains unaligned, untrimmed CDSs for all genes with at least 2 sequences for the 12 Drosophila species (where each represented species only has one sequence; species with paralogs were removed)
- trimmed contains the final sequence files used in concatenations and individual gene runs. Within trimmed is individual_trees, which contains the .nwk format trees used to run codeml for each individual gene. 
- trimmed_originals contains the final sequence files (same as above) but with the original gene IDs instead of just species names like the ones above.

codeml_output_individual_genes.zip:
Contains model 0 output (model = 0, NSsites = 0) for each individual gene, i.e. where each gene is assigned one dN/dS value for the entire tree. The genes are separated into their categories in the folders devo_codeml_output, nonplei_codeml_output, and plei_codeml_output. In each of those respective folders, there is:
- grepfile.txt: has results of grep command used to pull out omega value from each file
- [category]_dnds_values.txt: table with two columns, gene ID and omega value for that gene
- [category]_nodnds_values.txt: list of genes for which this codeml run did not produce an omega value. 

In scripts:

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
Obtains values for McDonald-Kreitman tests. Uses Table S3 from Fraisse et al, 2017 and lists of genes of interest to output 1) a list of genes of interest missing in Table S3 and 2) a table of values for the genes of interest found in Table S3. Again, file names are hard coded. 

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