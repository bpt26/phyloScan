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

"""
This program scans the PhyloP track for regions of high divergence immediately followed by conservation, or vice versa.
The parameters are:
	- flankLen - how long should the searched flanking region be at minimum in nucleotides
	- flankThreshold - how low should the average PhyloP score across that flanking region be
	- consLen - how long should the conserved region be at minimum in nucleotides
	- consThreshold - how high should the average PhyloP score across that conserved region be
"""

#########################
##### MAIN FUNCTION #####
#########################

def phyloScan():

	flankLen = float(sys.argv[1])
	flankThreshold = float(sys.argv[2])
	consLen = float(sys.argv[3])
	consThreshold = float(sys.argv[4])

	myOut = ''
	flank = False
	cons = False
	trackLen = flankLen+consLen

	flankScores = []
	consScores = []

	entryCount = 0
	
	for chrom in ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','X']:
		nextStart = 0
		myOutString = 'chrom\tflankStart\tconsStart\tconsEnd\tflankScore\tconsScore\n'
		for line in gzip.open('chr'+chrom+'.phyloP100way.wigFix.gz'):
			splitLine = (line.strip()).split()
			if splitLine[0].startswith('fixedStep'):
				if splitLine[2].startswith('start='):
					myStart = int(splitLine[2].split('=')[-1])
				else:
					print(splitLine)
			else:
				myStart += 1
				if len(flankScores) < flankLen:
					flankScores.append(float(line.strip()))
				elif len(consScores) < consLen:
					consScores.append(float(line.strip()))
				else:
					flankScores.pop(0)
					flankScores.append(consScores.pop(0))
					consScores.append(float(line.strip()))
				if myStart > nextStart and checkScores(flankScores, flankThreshold, consScores, consThreshold):
					myOutString += joiner([chrom, int(myStart)-int(flankLen)-int(consLen), int(myStart)-int(consLen), int(myStart), getAvg(flankScores), getAvg(consScores)])+'\n'
					entryCount += 1
					print(entryCount, myStart, flankScores, consScores)
					nextStart = myStart+flankLen+consLen

			#print(flankScores, consScores)
			if myStart % 1000000 == 0:
				print(myStart)
		open('chr'+chrom+'.phyloScan.'+str(flankLen)+'.'+str(flankThreshold)+'.'+str(consLen)+'.'+str(consThreshold)+'.txt','w').write(myOutString)
		sys.stderr.write("Finished chr"+chrom+'\n')


def getAvg(myList):
	myReturn = 0.0
	for k in myList:
		myReturn += k
	return(myReturn/float(len(myList)))


def checkScores(flankScores, flankThreshold, consScores, consThreshold):
	f = 0.0
	for k in flankScores:
		f += k
	if f > flankThreshold*len(flankScores):
		return(False)

	c = 0.0
	for k in consScores:
		c += k
	if c < consThreshold*len(consScores):
		return(False)
	return(True)



def joiner(entry):
    newList = []
    for k in entry:
        newList.append(str(k))
    return('\t'.join(newList))

def main():
    phyloScan()

if __name__ == "__main__":
    """
    Calls main when program is run by user.
    """
    main();
    raise SystemExit


        













