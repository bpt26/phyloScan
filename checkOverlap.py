#!/usr/bin/env python3
# Name: Bryan Thornlow
# Date: 7/31/2017
# messerBootstrap.py

import sys
import os
import time
import random
import numpy
import gzip
import math

#########################
##### MAIN FUNCTION #####
#########################

def checkOverlap():
    coordToGene = {}
    for line in open('hg19-tRNAs.bed'):
        splitLine = (line.strip()).split('\t')
        for k in range(int(splitLine[1]),int(splitLine[2])+1):
            coordToGene[str(splitLine[0])+'-'+str(k)] = splitLine[3]

    for line in open('histones.bed'):
        splitLine = (line.strip()).split('\t')
        for k in range(int(splitLine[1]),int(splitLine[2])+1):
            coordToGene[str(splitLine[0])+'-'+str(k)] = splitLine[3]

    for chrom in ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','X']:
        for line in open('chr'+chrom+'.phyloScan.15.0.-3.0.30.0.2.0.txt'):
            splitLine = (line.strip()).split('\t')
            mytRNA = ''
            if not splitLine[0] == 'chrom':
                splitLine[0] = 'chr'+splitLine[0]
                splitLine[1] = splitLine[1].split('.')[0]
                for k in range(int(splitLine[1]),int(splitLine[3])):
                    if splitLine[0]+'-'+str(k) in coordToGene:
                        mytRNA = coordToGene['chr'+chrom+'-'+str(k)]
                if mytRNA == '':
                    print(splitLine[0]+':'+splitLine[1]+'-'+str(splitLine[3]))
                else:
                    print(mytRNA)



def joiner(entry):
    newList = []
    for k in entry:
        newList.append(str(k))
    return('\t'.join(newList))

def main():
    checkOverlap()

if __name__ == "__main__":
    """
    Calls main when program is run by user.
    """
    main();
    raise SystemExit


        















