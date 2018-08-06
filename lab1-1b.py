#import matplotlib.pylot as plt
import random as rnd
import os

#===============================================================================
# read the instancedata given a file name. Returns n = no. of items,
# c = capacity, vs = list of item values, ws = list of item weights
#===============================================================================

def read_kfile(fname):
	with open(fname, 'rU') as kfile:
		lines = kfile.readlines()				#reads the whole file
	n = int(lines[0])							#1st line = number of items
	c = int(lines[n+1])							#last line capacity, convert to int
	vs = []
	ws = []
	lines = lines[1:n+1]						#removes first and last line to read items
	for l in lines:
		numbers = l.split()						#converts the string into a list
		vs.append(int(numbers[1]))				#appends value, need to convert to int
		ws.append(int(numbers[2]))				#appends weight, need to convert to int
	return n, c, vs, ws
	
#get the directory where the file is located
dir_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(dir_path)						#change the working directory so we can read the file

knapfile= 'knap20.txt'
nitems, cap, values, weights = read_kfile(knapfile)

#===============================================================================
# pltplot(values, weights, 'gd')
# plt.xlabel('Weights:')
# plt.ylabel('Values:')
# plt.figure()
# plt.show()
#===============================================================================

def random_sol(n):
	list = []
	for i in range(n):
		list.append(rnd.randint(0,1))
	return list

def evaluate(sol):

	totVal = 0
	totWeight = 0
	
	for i in range(len(sol)):
		if(sol[i] == 1):
			totVal += values[i]
			totWeight += weights[i]
	return totVal, totWeight

def random_search(tries):
	
	currBestSoln = 0
	currBestSolnVal = 0
 	currBestSolnWeight = 0
	
	for i in range(tries):
		currSoln = random_sol(nitems)
		totVal, totWeight = evaluate(currSoln)
		if (totVal >= currBestSolnVal and totWeight <= cap):
			currBestSoln = currSoln
			currBestSolnVal = totVal
			currBestSolnWeight = totWeight

	return currBestSoln, currBestSolnVal, currBestSolnWeight



randomSolns = random_sol(25)
print randomSolns

print

rSoln, rVal, rWeight = random_search(1000)
print "Solution: ", rSoln, "Total Value: ",  rVal, "Total Weight: ", rWeight

print



