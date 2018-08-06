# This script requires a couple of libraries to be installed and loaded
import matplotlib.pyplot as plt
import numpy as np
import math
import os
import copy
import random as rnd
import numpy as np
from scipy.spatial import distance


# Open the file
def read_cfile(fname):
    with open(fname, 'rU') as cfile:
        lines = cfile.readlines()  # reads the whole file
    n = int(lines[0])  # 1st line = number of items
    red = []
    green = []
    blue = []
    col = []
    lines = lines[1:n + 1]  # removes first and last line to read items
    for l in lines:
        numbers = l.split()  # converts the string into a list
        col.append([float(numbers[0]), float(numbers[1]), float(numbers[2])])
        red.append(float(numbers[0]))  # appends red, need to convert to double
        green.append(float(numbers[1]))  # appends green, need to convert to double
        blue.append(float(numbers[2]))  # appends blue, need to convert to double
    return n, col, red, green, blue

# get the directory where the file is located
dir_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(dir_path)  # change the working directory so we can read the file

coloursfile = 'Colours.txt'
nitems, col , red, green, blue = read_cfile(coloursfile)

size = 10; # number of colours

# Initialise colours and permutation.
# Here some basic code is given so that plot_colours maybe called 
# but the colours should be read from file 
# and the permutation computed with some algorithm.

colours = []
for i in range(0, size):
    colours.append (
        [
            0.1,
            0.2,
            0.3,
        ]
    )
permutation = np.arange(size)

# Display the colours in the order of the permutation in a pyplot window 
def plot_colours(colours, permutation):

    assert len(colours) == len(permutation)
    
    ratio = 10 # ratio of line height/width, e.g. colour lines will have height 10 and width 1

    img = np.zeros((ratio, len(colours), 3))

    for i in range(0, len(colours)):
        img[:, i, :] = colours[permutation[i]]

    fig, axes = plt.subplots(1, figsize=(8,4)) # figsize=(width,height) handles window dimensions
    axes.imshow(img, interpolation='nearest')
    axes.axis('off')
    plt.show()
    

def swao
    
    
def findEclidianDistance(len, sol):

    total = 0

    for i in range(len):
    
        var1 = col[i+1][0] - col[i][0]
        var2 = col[i+1][1] - col[i][1]
        var3 = col[i+1][2] - col[i][2]

        var1 = np.power(var1, 2)
        var2 = np.power(var2, 2)
        var3 = np.power(var3, 2)
        
        tot = var1 + var2 + var3
    
        distance = math.sqrt(tot)

        total = total + distance
        
        d = total

    return d

    
# Solution for first improvement hill climb
def firstImpovementHillClimb(iter):
    
    listLen = 5
    iterations = iter
    solution = col[:]
    curSol = copy.deepcopy(solution)
    fiSol = copy.deepcopy(solution)
    
    odist = findEclidianDistance(listLen, solution)
    
    print "First Improvement Hill Climb Starting... \n"
    
    for x in range(iter):
            
        for i in range(listLen):
            
            R1 = rnd.randint(0, listLen)
            R2 = rnd.randint(0, listLen)
            
            curSol[listLen] = 0
            print curSol [listLen]
            
            distance = findEclidianDistance(listLen, curSol)
    
    return odist, distance, fiSol


# display colours
#plot_colours(colours, permutation)
# to save image, use save button in window

odist, newdist, returnSol1 = firstImpovementHillClimb(10)
print "Original Distance: ", odist
print "New Distance: ", newdist
print "Return Solution: ", 


















