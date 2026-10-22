# A haplotype in the *SCN5A* promoter — a guided undergraduate research project

**A guided undergraduate research project of the Chronomic Medicine Group, in a workbench that runs entirely in
the browser.** In 2012, a study of one family found two variants in the *SCN5A* promoter — rs41310749 and
rs41310239 — reported them to be in complete linkage disequilibrium, and showed they tracked arrhythmia
severity among carriers of an *SCN5A* loss-of-function mutation. The survey that found them covered 2.8 kb.

Over eleven stages the student finds out what those two variants actually mark: an 18-variant haplotype
spanning **50.6 kb**, recovered with identical boundaries from the 1000 Genomes short-read panel and from 462
independently assembled long-read haplotypes of the human pangenome. They work out that it is not archaic,
carries no structural variation, and is thirteen times commoner in South Asians than in Africans. Then they
look for an effect — and the last stage is the one the project exists for.

It needs no programming experience. The guide teaches the Linux terminal, `bcftools`, PLINK 2 and R as the
project needs them, and everything runs in the browser: nothing is installed, and no data leave the computer.

The site is built from the [Bioinformatics workbench](https://github.com/comparativechrono/bioinformatics-workbench)
of the same group — the same notebooks (R and Python), terminal, Files tab, Databases tab, IDEs and AI
assistant — with a guide in the left pane in place of the workbench's help (the help is still there, behind
**Help**).

---

## The stage that makes the project worth doing

By stage 9 the student has a clean result: four cardiac traits associated with the haplotype at P < 10⁻⁴, and
nothing at all for five circadian and sleep traits in studies of several hundred thousand people. By the middle
of stage 10 they have apparently shown that the cardiac associations are independent of the locus's famous lead
variant, with P down to 1.4 × 10⁻⁴, consistently across every variant of the block.

Then they test the test. Twenty lines of simulation show that, at this locus — which carries **three**
independent signals, not one — that diagnostic rejects **86% of the time for a variant with no effect at all**,
with a median false-positive statistic just below the one they obtained. Conditioning properly on all three
signals leaves QRS duration and the QT interval null, Brugada syndrome at P = 0.041 by way of a sequence that
moves eight orders of magnitude, and only atrial fibrillation stable, at P = 0.011 — which does not survive
correction for six traits.

So the project's honest conclusion is that the haplotype is real, replicated, dated and structurally
characterised, and that **its cardiac effect cannot be resolved from public summary statistics**. The student
reaches a wrong answer, catches it themselves, and learns the thing most worth learning: that a P-value is only
as good as its null hypothesis, and the null is the part nobody checks.

The guide is built so this happens by design. Stage 10 asks the student to write down their conclusion *before*
running the simulation, and the logbook instructions say, in as many words, not to tidy that entry up
afterwards.

---

## Contents

1. [The guide](#the-guide)
2. [The workbench](#the-workbench)
3. [The data](#the-data)
4. [Running it locally](#running-it-locally)
5. [Building the site](#building-the-site)
6. [What a student produces](#what-a-student-produces)
7. [Credits and licence](#credits-and-licence)

---

## The guide

Twelve weeks, eleven stages, in the left pane. Each has a reading list, commands to run, numbers to check
against, a "think" question, a logbook prompt, and a checklist that fills in as it is ticked.

| Stage | Title | What the student does |
| --- | --- | --- |
| — | **The science** | The heart's sodium channel; what a haplotype is; why the circadian question is here |
| 1 | **Two variants** | The terminal; VCF files; genome builds and the 41,491-base offset; the 2012 paper |
| 2 | **Two thousand five hundred genomes** | The 1000 Genomes panel; PLINK 2; allele frequencies by population — and the African anomaly |
| 3 | **Measuring linkage** | D, D′ and r² by hand on 5,008 chromosomes; why two measures of the same thing say 1.0 and 0.1 |
| 4 | **How far does it reach?** | Scanning the whole 500 kb; discovering that pooling populations hides the block entirely |
| 5 | **The haplotype itself** | Splitting carriers from non-carriers; finding the 18 defining variants and the 50.6 kb |
| 6 | **Where in the world** | 26 populations; extended haplotype homozygosity; reading haplotype length as age |
| 7 | **Reading it with long reads** | Replicating the whole analysis in the pangenome; the repeat short reads describe five ways |
| 8 | **What is on the haplotype** | VEP annotation; testing it against a Neanderthal; GTEx, and what "no eQTL" does not mean |
| 9 | **Does it matter? Heart and clock** | Eleven sets of GWAS summary statistics; the build conversion and the allele flip |
| 10 | **Is it a signal of its own?** | Conditional analysis; building the standard test; simulating it; discovering it over-rejects |
| 11 | **Write it up** | Structure, figures, how to write a limitation, and making the analysis reproducible |

Plus three reference pages: **the project data** (every file, its provenance and what was filtered out), **the
reading list** (twenty papers, each with a note on what to take from it) and a **glossary** of every term, each
tagged with the stage where it first matters.

## The workbench

In the right pane, all running in the browser via WebAssembly:

- **Terminal** — bash with `bcftools`, `samtools`, `tabix`, **PLINK 2**, and the usual Unix tools.
- **Notebook** — Jupyter-style notebooks in R (webR) and Python (Pyodide). Each stage has a button that makes
  or opens its own notebook.
- **Files** — a file manager over the browser's storage, with upload and download.
- **Databases** — Ensembl, dbSNP, GTEx, NCBI and Europe PMC, with the project's variants as ready examples.
- **IDE** — editors for R and Python.
- **AI** — an assistant that knows what the project is and is told to help the student reason rather than hand
  over answers.

Work is saved in the browser as the student goes. Nothing is uploaded anywhere.

## The data

Read-only in `/data/examples/scn5a` inside the workbench, and in `data/examples/scn5a/` in this repository
(see its own `README.md` for the full description):

| Folder | What it is |
| --- | --- |
| `1000g/` | the 1000 Genomes 30× phased panel, 2,504 unrelated people, chr3:38.4–38.9 Mb, MAF ≥ 0.01 (2,392 records) |
| `hprc/` | the same window from the HPRC release 2 pangenome graph: 231 samples, 462 assembled haplotypes, 6,160 records |
| `gwas/` | summary statistics for six cardiac and five circadian traits, cut to the window, with their accessions and builds |
| `annotation/` | the haplotype's variants and their annotation, the Neanderthal alleles, the EHH curves, the GWAS Catalog associations, and the stage-10 diagnostics |

The derived tables are the *answers* to parts of the project, so that a student can check their own work — the
guide says in each stage to do the analysis first and compare afterwards.

Every number the guide asks a student to reproduce is itself checked against the bundle by a script in the
analysis repository, so the guide and the analysis cannot drift apart.

## Running it locally

```sh
git clone https://github.com/comparativechrono/chronomics-project-26-4
cd chronomics-project-26-4
python3 serve.py          # then open http://localhost:8000
```

The site needs to be served rather than opened as a file, because it sets the cross-origin isolation headers
that WebAssembly threading requires. `serve.py` does that; so does GitHub Pages, via `isolation-sw.js`.

## Building the site

`index.html` is generated. To change the guide, edit the pages in `build/help/` and rebuild:

```sh
python3 build/make_page.py        # writes index.html from build/template.html + build/help/*.html
python3 build/make_starters.py    # writes the starter notebooks in data/starter/
```

Each help page carries its metadata in an HTML comment on the first line — `id`, `title`, `stage`, whether it
gets a tab, its tab label, a one-line summary and search keywords. The build collects them, writes the tab row
and the search index, and inlines everything into a single page.

## What a student produces

By week 12: a paper with an abstract, methods, results and discussion; four figures; a reproducibility package
whose scripts run from a clean start; and a logbook — including, if they have done it properly, the entry where
they wrote down a conclusion that turned out to be wrong.

## Credits and licence

Built by the **Chronomic Medicine Group** on the group's
[Bioinformatics workbench](https://github.com/comparativechrono/bioinformatics-workbench). The workbench's
third-party components and their licences are listed in `THIRD_PARTY.md` and on the site's **Credits** page.

The data are public and belong to the projects that produced them — the 1000 Genomes Project, the Human
Pangenome Reference Consortium, GTEx, the Max Planck Institute for Evolutionary Anthropology, Ensembl and the
cohorts behind the eleven genome-wide association studies. Cite them as those projects ask; the accessions are
in `data/examples/scn5a/gwas/sources.tsv` and in the guide's **Data** page.

The guide and the site's own code may be reused freely for teaching.
