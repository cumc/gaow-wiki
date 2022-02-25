# About PLINK file format

[From a slack discussion initialized by a student in the lab]

PLINK format, in particular the bed/fam/bim bundle for genotype data, is one of the most popular format to store genotype information, amount a couple of others such as VCF (and derivatives from it) and bgen.

PLINK is like a swiss army knife for statistical genetics --- it does lots of extremely useful routine data analysis particularly data cleaning and exploratory analysis. That's why it is easy to start an analysis in PLINK format in order to use features offered in PLINK to understand the basics of data.

I think a general approach in learning (maybe anything) is to unbox the black box through looking at some simple examples. My suggestion is, try to install snpStats package in R and use this function:

https://www.rdocumentation.org/packages/snpStats/versions/1.22.0/topics/read.plink

on a small data-set here:

https://github.com/statgenetics/orientation/tree/main/data/LMM_MWE

the `genotype21_22` data bundle. See in R what you get!

In essence, `fam` file contains sample information, `bim` file contains variant information, both in plain text format that you can open with a **text editor** (in case you did not realize!). They only have a few columns so it should be easy to understand if you look at PLINK documentation. `bed` file is a sample by variant matrix of genotypes, but saved in binary format, which may look like a blackbox. That's why I suggested loading it with tools such as the aforementioned R package to look into it.

I would also like to point out that PLINK has a few types of file bundles. Most popular are bed/bim/fam (best compression with bed being a binary file), and ped/map (pure text format, stemmed from the traditional LINKAGE analysis software input). These bundles contain the same information and can be converted between each other using PLINK.
