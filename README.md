# phyloScan
scans phyloP data for mutational signatures (in development)

to run:
- first run *dloadPhyloP.sh* as this will download the phyloP tracks to be parsed
- then run *phyloScan.py flankLength flankThreshold consLength consThreshold* to pick up your desired signatures.
- ^for example, running *phyloScan.py 15 -3 40 2* would give you all the regions in the genome where there is a region 15 nucleotides long with an average phyloP score of less than or equal to -3, immediately followed by a conserved region 40 nucleotides long with an average phyloP score of greater than or equal to 2.
- *checkOverlap.py* (may need to modify within depending on your arguments for *phyloScan.py*) will report all of the regions that overlap tRNA genes and histones, and will also print any regions that do not overlap with genes in these families in a format that allows for easy copy/pasting into the genome browser to view what is going on at that region
