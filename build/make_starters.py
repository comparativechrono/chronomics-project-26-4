#!/usr/bin/env python3
"""Write the notebooks a new user finds in ~/notebooks: site/data/starter/*.ipynb

Run:  python3 build/make_starters.py
"""
import json
import os
import uuid

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
SITE = ROOT if os.path.isdir(os.path.join(ROOT, 'assets')) else os.path.join(ROOT, 'site')
OUT = os.path.join(SITE, 'data', 'starter')

PY = {'kernelspec': {'name': 'python3', 'display_name': 'Python 3 (ipykernel)', 'language': 'python'},
      'language_info': {'name': 'python', 'file_extension': '.py', 'mimetype': 'text/x-python'}}
R = {'kernelspec': {'name': 'ir', 'display_name': 'R', 'language': 'R'},
     'language_info': {'name': 'R', 'file_extension': '.r', 'mimetype': 'text/x-r-source'}}


def lines(s):
    s = s.strip('\n')
    out = s.split('\n')
    return [l + '\n' for l in out[:-1]] + [out[-1]]


def md(s):
    return {'cell_type': 'markdown', 'id': uuid.uuid4().hex[:8], 'metadata': {}, 'source': lines(s)}


def code(s):
    return {'cell_type': 'code', 'id': uuid.uuid4().hex[:8], 'metadata': {}, 'execution_count': None, 'outputs': [], 'source': lines(s)}


def nb(meta, cells):
    m = dict(meta)
    m['workbench'] = {'made_with': 'A haplotype in the SCN5A promoter – the SCN5A haplotype project (from the Bioinformatics workbench)', 'kind': 'starter'}
    return {'cells': cells, 'metadata': m, 'nbformat': 4, 'nbformat_minor': 5}


WELCOME_PY = nb(PY, [
    md('''# Python in your browser

This is a Jupyter-style notebook. Python runs **inside this web page** – nothing is installed, and nothing you
type leaves your computer.

* Run a cell: click ▶ or press **Shift+Enter** (it moves to the next cell).
* Add cells with **+ Code** and **+ Text**; text cells use Markdown (`# heading`, `**bold**`, `- list`).
* The notebook is saved as you work, among your files (`~/notebooks`). **Download** gives you the `.ipynb` file,
  which opens in Jupyter, JupyterLab, VS Code or Google Colab.

Run the cells below one by one.'''),
    code('''name = "workbench"
print(f"Hello from Python in the {name}!")'''),
    md('''## A table with pandas

The workbench has example data in `/data/examples` (read-only). This table describes 5,481 yeast genes.'''),
    code('''import pandas as pd

genes = pd.read_csv("/data/examples/tables/yeast_genes.csv")
genes.head()'''),
    code('''# how long are the proteins of essential (1) and non-essential (0) genes?
genes.groupby("essential")["protein_length"].describe()'''),
    md('''## A plot with matplotlib'''),
    code('''import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(6, 3.5))
for value, label in [(0, "not essential"), (1, "essential")]:
    ax.hist(genes.loc[genes.essential == value, "protein_length"], bins=60, range=(0, 2000), alpha=0.6, label=label)
ax.set_xlabel("protein length (amino acids)")
ax.set_ylabel("genes")
ax.legend()
plt.show()'''),
    md('''## Sequences with Biopython

Packages that are part of Pyodide (Biopython, NumPy, SciPy, scikit-learn, NetworkX …) load by themselves the
first time you import them. Others can often be added with `%pip install NAME`.'''),
    code('''from Bio import SeqIO

for record in SeqIO.parse("/data/examples/sequences/myoglobins.fasta", "fasta"):
    print(f"{record.id:15} {len(record.seq):4} aa   {record.seq[:30]}…")'''),
    md('''## The terminal's programs, from a cell

A line that starts with `!` runs in the workbench's shell, with the same programs as the Terminal tab
(samtools, bcftools, minimap2, …). A cell whose first line is `%%bash` is all shell commands.'''),
    code('''!samtools faidx /data/examples/reads/reference.fa human_CYP2C19:11590-11640'''),
    code('''%%bash
bcftools view -H /data/examples/variants/NA12878.calls.vcf.gz | cut -f 1-5 | head -5'''),
    md('''## Data from the web

Web services that allow it (EBI, UniProt, Ensembl, NCBI, the PDB …) can be called with `requests`. The
**Databases** tab has many of them ready to use, and writes the code for you ("Send to notebook").'''),
    code('''import requests

r = requests.get("https://rest.uniprot.org/uniprotkb/P02185.fasta")
print(r.text)'''),
    md('''## Next

* The **Help** pane (left) has a guide to every tab and program – search it for anything.
* **Notebooks → New Python notebook** starts a fresh one; **New R notebook** gives you R.
* Stuck on an error? Each cell has an **Ask AI** button (set up the assistant in the AI tab first).'''),
])

WELCOME_R = nb(R, [
    md('''# R in your browser

This notebook runs **R** (webR: R compiled for the web browser). Nothing is installed, and your code and data
stay on your computer.

* Run a cell with ▶ or **Shift+Enter**. R starts in the background when this notebook opens; the first run waits for it – a few seconds.
* Packages: `install.packages("ggplot2")`, or simply `library(ggplot2)` – packages are downloaded the first
  time they are used in a visit (CRAN from repo.r-wasm.org, Bioconductor from bioc-release.r-universe.dev).
* Download the notebook (`.ipynb`) to open it in Jupyter with the R kernel (IRkernel).'''),
    code('''x <- c(4, 8, 15, 16, 23, 42)
mean(x)
summary(x)'''),
    md('''## A data frame

The example table of 5,481 yeast genes, read with `read.csv`.'''),
    code('''genes <- read.csv("/data/examples/tables/yeast_genes.csv")
dim(genes)
head(genes[, c("orf", "gene", "essential", "protein_length", "location")])'''),
    code('''# genes per cell compartment, most common first
sort(table(genes$location), decreasing = TRUE)[1:8]'''),
    md('''## Plots

Base R graphics work straight away:'''),
    code('''boxplot(protein_length ~ essential, data = genes, log = "y",
        names = c("not essential", "essential"), ylab = "protein length (aa)",
        col = c("#9ecae1", "#fdae6b"))'''),
    md('''… and so does ggplot2 (the first `library(ggplot2)` downloads it – give it half a minute):'''),
    code('''library(ggplot2)
ggplot(genes, aes(x = protein_length, fill = factor(essential))) +
  geom_histogram(bins = 60, alpha = 0.7, position = "identity") +
  scale_x_continuous(limits = c(0, 2000)) +
  labs(x = "protein length (aa)", y = "genes", fill = "essential") +
  theme_minimal()'''),
    md('''## Shell commands from an R notebook

R itself cannot start programs here, but a cell whose first line is `%%bash` runs in the workbench's shell,
with the terminal's programs:'''),
    code('''%%bash
seqtk comp /data/examples/sequences/myoglobins.fasta | cut -f 1,2 | head'''),
    md('''## Bioconductor (optional – it downloads several packages)

```r
library(Biostrings)
myo <- readAAStringSet("/data/examples/sequences/myoglobins.fasta")
myo
```

Copy it into a new cell to try it. Packages that need compiled system libraries may not exist for the
browser; the Help pane lists what to expect. DESeq2 and edgeR do work – the recipe
**RNA-seq: reads to differential expression** in the Help pane is a whole analysis with them.'''),
])


START_HERE = nb(R, [
    md('''# Start here: notebooks in the SCN5A haplotype project

This is an R notebook, running **inside this web page**. Nothing is installed and nothing you type leaves
your computer.

* Run a cell: click ▶ or press **Shift+Enter**.
* Add cells with **+ Code** and **+ Text**; text cells use Markdown.
* Your notebooks are saved in this browser as you work.

The guide on the left takes you through the project in stages, and each stage has a button that makes you a
notebook of its own. This one is just to get you started.

Try it: how common are the project\'s two variants?'''),
    code('''v <- read.delim("/data/examples/scn5a/variants.tsv")
head(v[, c("variant", "pos_GRCh38", "pos_GRCh37", "ref", "alt", "role")], 4)'''),
    md('''Every variant has **two** positions, because a position means nothing without saying which version -
which *build* - of the human reference genome it is on. Check the difference between them:'''),
    code('''unique(v$pos_GRCh37 - v$pos_GRCh38)'''),
    md('''One number, 41,491, for every variant. That is the offset between GRCh37 and GRCh38 **along this
stretch of chromosome 3 and nowhere else**. Write it down; you will need it in stage 9, and a project of this
kind has sunk on a build mix-up before now.

Now the people. The 1000 Genomes panel in this bundle has 2,504 of them:'''),
    code('''samples <- read.delim("/data/examples/scn5a/1000g/samples.tsv")
nrow(samples)
table(samples$superpopulation)'''),
    md('''Write here, in this text cell, one sentence about what you notice. (Double-click to edit.)

---

A cell whose first line is `%%bash` runs in the terminal\'s shell, with its programs:'''),
    code('''%%bash
ls /data/examples/scn5a
bcftools view -H -r chr3:38651526 /data/examples/scn5a/1000g/scn5a_locus.vcf.gz | cut -f 1-5'''),
    md('''Your notebooks are saved in this browser as you work. **My files → Download all my files** (top right)
keeps a copy. The Python and R welcome notebooks have more to practise on, with other example data.'''),
])


def main():
    os.makedirs(OUT, exist_ok=True)
    for name, data in [('start-here.ipynb', START_HERE), ('welcome-python.ipynb', WELCOME_PY), ('welcome-r.ipynb', WELCOME_R)]:
        with open(os.path.join(OUT, name), 'w', encoding='utf-8') as fh:
            json.dump(data, fh, indent=1, ensure_ascii=False)
            fh.write('\n')
        print('wrote', name)


if __name__ == '__main__':
    main()
