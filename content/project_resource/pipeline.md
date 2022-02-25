# Pipelines and benchmarks made by members of the lab

This is a curated list of pipelines and computational benchmarks made in the lab, at the level of maturity and quality of engineering good enough to be used by other research groups in the community.

## GWAS enrichment and fine-mapping

- [Pipeline for enrichment and fine-mapping](https://github.com/gaow/fine-mapping) using annotation and GWAS summary statistics. It implements enrichment analysis via `torus` and fine-mapping using summary statistics and LD panel from reference genotype files via `susieR`, `CAVIAR` and `FINEMAP`.
    - Gao Wang and Min Qiao

## eQTL association and multivariate analysis

- [Multivariate Adaptive Shrinkage (MASH) pipeline](https://github.com/stephenslab/gtexresults) currently works on GTEx data. It contains a [summary statistics formatting pipeline](https://github.com/stephenslab/gtexresults/blob/master/workflows/fastqtl_to_mash.ipynb) and a [MASH association analysis pipeline](https://github.com/stephenslab/gtexresults/blob/master/workflows/fastqtl_to_mash.ipynb). To see these pipelines in action, here is [an example analysis on GTEx V8 European only samples](https://github.com/gaow/mnm-gtex-v8/blob/master/analysis/European_QTL.ipynb).
    - Gao Wang

## Linear mixed model analysis for UK Biobank scale data-set

- [Linear mixed model](https://github.com/cumc/bioworkflows/blob/master/GWAS/LMM.ipynb), [LD clumping](https://github.com/cumc/bioworkflows/blob/master/GWAS/LD_Clumping.ipynb) and [extraction of targets identified](https://github.com/cumc/bioworkflows/blob/master/GWAS/Region_Extraction.ipynb).
    - Diana Cornejo and Yin Huang