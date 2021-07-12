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
`posii` takes fasta sequences and a position/slice then returns
the residues found there. If a residue(s) is also given,
`posii` will return the accessions of the sequences with the residue(s)
at that position/slice.

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
usage: posii <input.fasta> pos

positional arguments:
  pos         position (2) or slice (2:4)

optional arguments:
  -res RES    returns accessions with this residue at chosen position
  -tt TT      translation table to return amino acid position
  -perc       calculates % of each residue at chosen position
  -v          prints information to stderr
  -h, --help  show this help message and exit
```