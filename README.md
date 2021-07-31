# posii :dna::female_detective::abacus:

<centre>![Image](https://github.com/tomdstanton/posii/blob/master/posii.png)

_By Tom Stanton_ (he/him) :scientist: \
[![alt text][1.1]][1] [![alt text][6.1]][6] \
Issues/queries/advice?
[email me!](mailto:s1895738@ed.ac.uk?subject=[posii])

[1]: http://twitter.com/tomstantonmicro
[1.1]: http://i.imgur.com/tXSoThF.png (twitter icon with padding)
[6]: http://www.github.com/tomdstanton
[6.1]: http://i.imgur.com/0o48UoR.png (github icon with padding)

### Introduction :open_book:
* `posii` takes fasta and/or fastq sequences and a position/slice then returns
the residues found there. 
* If a residue(s) is also given, `posii` will return the accessions of the sequences with the residue(s)
at that position/slice.
* If given multiple sequences, `posii` can 
  calculate the percentage of each residue(s) at the given
  position/slice.


**If you found posii helpful, please cite:**
```
posii - Position Interrogator
Thomas David Stanton, 2021
https://github.com/tomdstanton/posii
```
### Dependencies :toolbox:
* python >=3.7

### Installation :gear:
```sh
git clone --recursive https://github.com/tomdstanton/posii && cd posii && python setup.py install
```
### Usage :computer:
```sh
usage: posii <input.fastx> -pos

  -pos         position (2) or slice (2:4)

optional arguments:
  -res RES    returns accessions with this residue(s) at chosen position
  -tt TT      translation table to return amino acid position
  -perc       calculates % of each residue at chosen position
  -v          prints information to stderr
  -h, --help  show this help message and exit
```
**Woah there, there are some rules...**
* DNA is ALWAYS lower case. When searching for a 
  nucleotide residue at a position, use 'a' _not_ 'A'.
  
* You can mix nucleotide and amino acid inputs, however using `-tt` will only translate
  DNA to protein, not reverse-translate.
  

### Cookbook :cook:
return 420th residue for all sequences in a folder of fasta files: `posii genes/*.fasta -pos 420`
concatenate gene and protein sequences, and return the 140th amino acid using the bacterial codon table: `sh cat protein.faa gene.faa | posii -pos 140 -tt 11`
check potential start codons in a file of CDS: `posii CDS.fasta -pos 1:3`
return accessions of CDS with an atg start codon: `posii CDS.fasta -pos 1:3 -res atg`
concatenate DNA fasta files and return accessions with amino acid F in position 140 using the bacterial codon table: `sh cat genes/*.fasta | posii -pos 140 -tt 11 -res F`
calulate the percentage of the 420th residue in a sequence alignment: `posii gene_aligned.fasta -pos 420 -perc`
return accessions in a sequence alignemnt that have the sequence KGGM at positions 140-144: `posii gene_aligned.fasta -pos 140:144 -res KGGM`

### Case uses 🔬
_Klebsiella pneumoniae_ ST258 clones have reduced
carbapenem susceptibility due to a GD-loop insertion
in the passive-diffusion outer-membrane protein (porin)
OmpK36 (OmpC). OmpK36 protein sequences from 
1000 random  _K. pneumoniae_ Genbank assemblies
were concatenated to a fasta file. We will align these
sequences with MUSCLE and pipe into posii so we can
examine how many of the sequences have this insertion.
```sh
cat OmpK36_multi.faa | muscle | posii -pos 159:166 -perc
G--GDTYG: 0.1%
G--G---D: 68.78%
GGDT---D: 1.43%
GG-D---D: 0.31%
GGDG---D: 22.21%
G--GDTYD: 0.1%
G--GD--D: 2.35%
GGD----D: 0.1%
G--GDT-D: 0.41%
GG-----D: 4.2%
```
