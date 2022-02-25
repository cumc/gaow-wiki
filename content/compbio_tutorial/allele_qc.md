# Allele flip when merging genotype data

## Problem

Suppose we have some genetic variants measured in two sets of individuals and we would like to merge these genotype data.
Ideally, a variant, given by `chrom`, `position`, `reference allele`, `alternative allele`, would easily merge if information between
two data-sets are consistent. That is, the variant has the same 4 quantities for the different data-sets. However in reality there are
a few problems:

- ***Scenario 1:*** When genotype data are given in PLINK format, there is no information on which allele is the reference and which is alternative allele.
   Instead all you get is "major" and "minor" allele, which is determined by the samples in the data-set. For example suppose a variant is:

   ```
   1:124235:A:G # chrom:pos:ref:alt
   ```

   and in the first data-set 60% alleles are `A`, whereas in the 2nd data-set only 45% are `A`. Then in the PLINK `bim` file the major allele will be
   A for data-set 1, and G for data-set 2. Even though in this case the two variants will appear 

   ```
   1:124235:A:G # chrom:pos:major:minor
   ```

   and 

   ```
   1:124235:G:A # chrom:pos:major:minor
   ```

   in different data-sets, they are still the same variant. Software such as PLINK will handle these major/minor allele inconsistency by internally flipping genotype coding
   when the variants are merged,
   as long as we make the variant ID the same for the two data-sets in PLINK `bim` file (via some simple programming) so PLINK knows they are the same variant.

- ***Scenario 2:*** Sometimes a variant, measured on different strand due to differences in genotyping platform, can have different allele representations. For example in the first data-set:

   ```
   1:124235:A:G
   ```

  and the second:

   ```
   1:124235:T:C
   ```

   but in fact these two variants are the same because alleles A/G on their complementary DNA strand is `T/C`. In practise what we do is to change the allele representation in the 2nd data to

   ```
   1:124235:A:G
   ```

   to match and be ready to merge with the first data-set. This is called strand flip. 

   Notice that the 2nd data-set may have `1:124235:C:T` which flips to `1:124235:G:A`, and falls in scenario #1 the major minor allele inconsistency which is straightforward to iron out with tools like PLINK. 

- ***Scenario 3:***  Complication arise when it comes to specificly A/T and C/G genotypes. Suppose a variant in the first data-set:

   ```
   1:124236:A:T
   ```

   and the second:

   ```
   1:124236:T:A
   ```

   If it is a strand flip, the 2nd data-set on the complementary strand is

   ```
   1:124236:A:T
   ```

   which can be directly merged with the first data-set. However, it can also be a major/minor allele inconsistency in which case we do not flip the strand but will rely on PLINK to flip the allele coding while it merges the data.
   **Since we cannot tell one situation from another, and the genotypes in these two situations will be handled differently**, in practice we simply remove variants with A/T alleles from consideration. 

   Same holds for C/G --- you can work that out yourself to verify

- Tri-allelic case, such as one data-set has `A:C` the other has `A:G`, or `C:G` etc.

## Implementation of a solution

The R code below is extracted from [FUSION](http://gusevlab.org/projects/fusion/) script by Hao Sun in our group:

```r
allele.qc = function(a1,a2,ref1,ref2) {
	# a1 and a2 are the first data-set
	# ref1 and ref2 are the 2nd data-set
	# Make all the alleles into upper-case, as A,T,C,G:
        a1 = toupper(a1)
        a2 = toupper(a2)
        ref1 = toupper(ref1)
        ref2 = toupper(ref2)
	# Strand flip, to change the allele representation in the 2nd data-set
	strand_flip = function(ref) {
		flip = ref
		flip[ref == "A"] = "T"
		flip[ref == "T"] = "A"
		flip[ref == "G"] = "C"
		flip[ref == "C"] = "G"
		flip
	}
	flip1 = strand_flip(ref1)
	flip2 = strand_flip(ref2)
	snp = list()
	# Remove strand ambiguous SNPs (scenario 3)
	snp[["keep"]] = !((a1=="A" & a2=="T") | (a1=="T" & a2=="A") | (a1=="C" & a2=="G") | (a1=="G" & a2=="C"))
	# Remove non-ATCG coding
	snp[["keep"]][ a1 != "A" & a1 != "T" & a1 != "G" & a1 != "C" ] = F
	snp[["keep"]][ a2 != "A" & a2 != "T" & a2 != "G" & a2 != "C" ] = F
	# as long as scenario 1 is involved, sign_flip will return TRUE
	snp[["sign_flip"]] = (a1 == ref2 & a2 == ref1) | (a1 == flip2 & a2 == flip1)
	# as long as scenario 2 is involved, strand_flip will return TRUE
	snp[["strand_flip"]] = (a1 == flip1 & a2 == flip2) | (a1 == flip2 & a2 == flip1)
	# remove other cases, eg, tri-allelic, one dataset is A C, the other is A G, for example.
	exact_match = (a1 == ref1 & a2 == ref2) 
	snp[["keep"]][!(exact_match | snp[["sign_flip"]] | snp[["strand_flip"]])] = F
	return(snp)
}
```

Each input `a1`, `a2`, `ref1`, `ref2` is a list of characters of `{ATCG}`.

### Example usage 1: merge summary statistics data with reference genotypes

In this application, `strand_flip` does not matter and only `sign_flip` matters. `sign_flip` is major/minor allele flip, and matters to the sign of z-scores

```r
qc = allele.qc( sumstat$A1 , sumstat$A2 , genos$bim[,5] , genos$bim[,6] )
# Flip Z-scores for mismatching alleles
sumstat$Z[ qc$sign_flip ] = -1 * sumstat$Z[ qc$sign_flip ]
sumstat$A1[ qc$sign_flip ] = genos$bim[qc$sign_flip,5]
sumstat$A2[ qc$sign_flip ] = genos$bim[qc$sign_flip,6]
# Remove strand ambiguous SNPs (if any)
if ( sum(!qc$keep) > 0 ) {
	genos$bim = genos$bim[qc$keep,]
	genos$bed = genos$bed[,qc$keep]
	sumstat = sumstat[qc$keep,]
}
```

### Example usage 2: merge two genotype data-set

When two data-sets are merged with PLINK, `sign_flip` (the major/minor allele flips) does not matter because PLINK will handle it internally. Only `strand_flip` matters and we have to fix the alleles for those that need a strand flip.

Suppose we have 12 same variants in 2 data-sets:

Data-set one:

   ```
1  22 rs9617549   0 10874444 C T
2  22 rs5747224   0 11122151 G A
3  22 rs2456393   0 11122417 G T
4  22 rs9617550   0 10874444 A G
5  22 rs5747225   0 11122151 T C
6  22 rs2456394   0 11122417 A C
7  22 rs199668908 0 11123683 A G
8  22 rs199674018 0 11125296 A T
9  22 rs538546296 0 15282439 C G
10 22 rs551794980 0 15283826 T A
11 22 rsxxxxxxxxx 0 15284000 A C
12 22 rsyyyyyyyyy 0 15285000 A C
   ```
Data-set two:

   ```
1  22 rs9617549   0 10874444 T C
2  22 rs5747224   0 11122151 A G
3  22 rs2456393   0 11122417 T G
4  22 rs9617550   0 10874444 T C
5  22 rs5747225   0 11122151 A G
6  22 rs2456394   0 11122417 T G
7  22 rs199668908 0 11123683 C T
8  22 rs199674018 0 11125296 T A
9  22 rs538546296 0 15282439 G C
10 22 rs551794980 0 15283826 T A
11 22 rsxxxxxxxxx 0 15284000 A G
12 22 rsyyyyyyyyy 0 15285000 C G
   ```

We can tell the variants are the same by `chr_pos`. For example the first variant: is from chromosome 22, and the start position is 10874444. Sometimes the variant ID (e.g.rs9617549) is not provided. 

For the 12 lines (examples) of the above 2 data-sets: 
		
		Line 1-3: Scenario 1
		Line 4-6: Scenario 2
		Line 7: The combination of scenario 1 and scenario 2.
				(Falls into scenario 1, after strand flip)
		Line 8-10: Scenario 3
		Line 11-12: Trialleic cases
We need to merge these 2 datasets together by `chr_pos`, then apply `allele.qc` onto the merged data. 

The `data_merge` should look like this:

```
	chr_pos	        V1.x	V2.x	V3.x	V4.x	V5.x	V6.x	V1.y	V2.y	V3.y	V4.y	V5.y	V6.y
1	22:rs9617549	22	rs9617549	0	10874444	C	     T	       22	rs9617549	0	10874444	T	C
2	22:rs5747224	22	rs5747224	0	11122151	G	     A	       22	rs5747224	0	11122151	A	G
3	22:rs2456393	22	rs2456393	0	11122417	G	     T	       22	rs2456393	0	11122417	T	G
4	22:rs9617550	22	rs9617549	0	10874444	A	     G	       22	rs9617549	0	10874444	T	C
5	22:rs5747225	22	rs5747224	0	11122151	T	     C	       22	rs5747224	0	11122151	A	G
6	22:rs2456394	22	rs2456393	0	11122417	A	     C	       22	rs2456393	0	11122417	T	G
7	22:rs199668908	22	rs199668908	0	11123683	A	     G     	   22	rs199668908	0	11123683	C	T
8	22:rs199674018	22	rs199674018	0	11125296	A	     T	       22	rs199674018	0	11125296	T	A
9	22:rs538546296	22	rs538546296	0	15282439	C     	 G	       22	rs538546296	0	15282439	G	C
10	22:rs551794980	22	rs551794980	0	15283826	T	     A	       22	rs551794980	0	15283826	T	A
11	22:rsxxxxxxxxx	22	rsxxxxxxxxx	0	15284000	A	     C	       22	rsxxxxxxxxx	0	15284000	A	G
12	22:rsyyyyyyyyy	22	rsyyyyyyyyy	0	15285000	A	     C	       22	rsyyyyyyyyy	0	15285000	C	G
```


And we then apply `allele.qc` as:

```
qc = allele.qc(data_merge[,'V5.x'] , data_merge[,'V6.x'] , data_merge[,'V5.y'], data_merge[,'V6.y'])

```
The interface of this merger, and how it works in detail can be found [Here](https://github.com/gaow/alzheimers-family/blob/master/notebook/20210224_Allele_QC_MWE_Analysis.ipynb).


**The results of testing the 12 SNPs are as expected**

1. `keep` would return FALSE for scenario 3 and triallelic cases, i.e. the last 5 examples.

2. `sign_flip` identifies those cases where scenario 1 is involved, i.e. TRUE for the first 3 variantes (scenario 1 only), the 7th variantes (combination of scanrio 1 and scenario 2), and scenario 3, lines 8-10.

2. `strand_flip` identifies those cases where scenario 2 is involved, i.e. TRUE for scenario 2 only (lines 4-6), the 7th variantes (combination of scanrio 1 and scenario 2), and scenario 3, line 8-10.

