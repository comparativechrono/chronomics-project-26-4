# The project data: the *SCN5A* promoter haplotype

Everything the project needs, read-only. The guide on the left of the page works through it in stages; the
"The project data" page of the guide describes each file, its provenance and what was filtered out. This file
is the short version.

**All positions here are on GRCh38.** Four of the eleven GWAS files are on GRCh37; across this locus the two
builds differ by exactly **41,491** bases, so `GRCh37 = GRCh38 + 41,491`. That offset holds here and nowhere
else in the genome.

The two variants the project starts from:

| variant | GRCh38 | GRCh37 | ref | alt |
| --- | --- | --- | --- | --- |
| rs41310749 | chr3:38,651,526 | chr3:38,693,017 | G | A |
| rs41310239 | chr3:38,650,537 | chr3:38,692,028 | A | G |

Both lie in the *SCN5A* promoter region. *SCN5A* is chr3:38,548,057–38,649,743 on the **minus** strand, so its
transcription start is its highest coordinate, 38,649,743; *SCN10A* is chr3:38,696,802–38,816,286, also minus.

## Folders

| Folder | Files | What they are |
| --- | --- | --- |
| `1000g/` | `scn5a_locus.vcf.gz` (+ `.tbi`) | Phased genotypes of the 1000 Genomes Project 30× release (NYGC, 20220422) across chr3:38,400,000–38,900,000, for the **2,504 unrelated** individuals, biallelic, minor allele frequency ≥ 0.01. **2,392 records.** One has the symbolic allele `<DEL>`, which some tools count and some drop. |
| | `samples.tsv` | sample, population, superpopulation for all 2,504 |
| | `unrelated.txt` | the sample IDs, one per line, for `bcftools view -S` |
| `hprc/` | `scn5a_locus.vcf.gz` (+ `.tbi`) | The same stretch from the Human Pangenome Reference Consortium release 2 Minigraph-Cactus graph, decomposed to one record per allele: **231 samples, 462 assembled haplotypes, 6,160 records**, indels of every size included. The phase here is observed, not inferred. |
| | `hprc_samples.csv` | the assembly samples and their populations |
| `gwas/` | eleven `*.tsv` files | Published GWAS summary statistics cut to the 500 kb window: six cardiac (PR interval, QRS duration, QT interval, resting heart rate, atrial fibrillation, Brugada syndrome) and five circadian (chronotype, morning person, sleep duration, insomnia, daytime napping). Column names and delimiters differ between studies — read each header. |
| | `sources.tsv` | accession, URL and **genome build** for each of the eleven |
| `annotation/` | `haplotype_variants.tsv` | The 21 variants of the haplotype: frequencies on and off it in both datasets, which dataset calls each one "defining", and the Ensembl Variant Effect Predictor output |
| | `genes.tsv` | *SCN5A* and *SCN10A*: coordinates, strand, description |
| | `archaic_alleles.tsv` | the Vindija Neanderthal genotype and read depth at each of the 21 positions |
| | `gwas_catalog_locus.tsv` | every association reported in the GWAS Catalog within the locus (266 unique study–trait–variant rows, 103 variants) |
| | `ehh_decay.tsv` | extended haplotype homozygosity against distance, by population and direction |
| | `tagging_diagnostic.tsv` | the stage 10 diagnostic for every variant and trait: lead variant, correlation with it, expected *z* and its standard error, residual and its P-value |
| | `gtex_eqtls.tsv`, `gtex_tagging.tsv` | GTEx v8 significant eQTLs of *SCN5A*/*SCN10A* that fall on the haplotype, and the same tagging diagnostic applied to the whole-blood expression signal |
| `variants.tsv` | | the two promoter variants and the 21 of the haplotype, on both builds |

The tables in `annotation/` are **answers** to parts of the project, kept here so you can check your own work
against them. Do each stage first and compare afterwards.

## Citing the data

- 1000 Genomes 30×: Byrska-Bishop M *et al.* *Cell* 2022;185:3426–3440.e19. doi:10.1016/j.cell.2022.08.004
- Pangenome: Liao WW *et al.* *Nature* 2023;617:312–324. doi:10.1038/s41586-023-05896-x; graph construction,
  Hickey G *et al.* *Nat Biotechnol* 2024;42:663–673. doi:10.1038/s41587-023-01793-w
- Vindija Neanderthal: Prüfer K *et al.* *Science* 2017;358:655–658. doi:10.1126/science.aao1887
- GTEx v8: GTEx Consortium. *Science* 2020;369:1318–1330. doi:10.1126/science.aaz1776
- GWAS summary statistics: the accessions in `gwas/sources.tsv`, via the NHGRI-EBI GWAS Catalog
- The study the project starts from: Park JK, Martin LJ, Zhang X, Jegga AG, Benson DW. *Heart Rhythm*
  2012;9:1090–1096. doi:10.1016/j.hrthm.2012.02.023

## What is not here

No individual-level phenotypes (none are public — which is why the project uses summary statistics), no
variants below 1% frequency in the short-read file, and no cardiac expression data with real power: GTEx finds
no eQTLs for *SCN5A* in heart at all, so the mechanism question cannot be settled with public data as it stands.
