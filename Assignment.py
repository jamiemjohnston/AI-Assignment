# This script requires a couple of libraries to be installed and loaded
import matplotlib.pyplot as plt
import numpy as np
import math
import os
import copy
import random as rnd


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
    
    
# Square two numbers
def square(x):
    
    z = x * x
    return z    
    
# Find eculidian distancw
def findDistance(X1, Y1, Z1, X2, Y2, Z2):
    
    param1 = X2 - X1
    param2 = Y2 - Y1
    param3 = Z2 - Z1

    p1Squ = square(param1)
    p2Squ = square(param2)
    p3Squ = square(param3)
    
    finalParam = p1Squ + p2Squ + p3Squ
    
    d = math.sqrt(finalParam)
    
    return d

# Find Euclidean distance
def findEclidianDistance(n, soln):

    totalDistance = 0
    
    scale = n * 3
    
    for i in range(scale):
    
        param1 = soln[i] - soln[i+3]
        param2 = soln[i+1] - soln[i+4]
        param3 = soln[i+2] - soln[i+5]
    
        p1Squ = square(param1)
        p2Squ = square(param2)
        p3Squ = square(param3)
        
        finalParam = p1Squ + p2Squ + p3Squ
        
        d = math.sqrt(finalParam)
        
        totalDistance = totalDistance + d
    
    return totalDistance

def sol(red,green,blue):
     
    list = []
    for i in range(1000):
        list.append(red[i])
        list.append(green[i])
        list.append(blue[i])
         
    return list

def rsol(n,red,green,blue):
    
    list = []
    
    return list
    
# Solution for first improvement hill climb
def firstImpovementHillClimb(iter):
    
    listLen = 50
    iterations = iter
    solution = col
    curSol = copy.deepcopy(solution)
    fiSol = copy.deepcopy(solution)
    
    odist = findEclidianDistance(listLen, solution)
    
    for x in range(iter):
            
        for i in range(listLen):
            
            checker = findEclidianDistance(listLen, curSol)
            
            R1 = rnd.randint(0, listLen)
            R2 = rnd.randint(0, listLen)
            
            if (R1 != R2):
                temp = solution[R1]
                solution[R1] = solution[R2]
                solution[R1] = temp
                
            
    
    distance = findEclidDistance(listLen, fiSoll)
    
    return odist, distance, fiSol

# Solution for first improvement hill climb
def firstImpovementHillClimbImproved():
    
    iterations = 50
    solution = sol(red, green, blue)
    cs = copy.deepcopy(solution)
    fi_solution = copy.deepcopy(solution)
    
    odist = findEclidianDistance(iterations, solution)
    
    for x in range(500):
            
        for i in range(iterations):
            
            for l in range(iterations):
            
                check = findDistance(cs[i], cs[i + 1], cs[i + 2], cs[l + 3], cs[l + 4], cs[l + 5])
                checker = findDistance(cs[i], cs[i + 1], cs[i + 2], cs[l + 6], cs[l + 7], cs[l + 8])
            
                if (checker < check):
                    tempA = cs[l + 3]
                    tempB = cs[l + 4]
                    tempC = cs[l + 5]
                    
                    cs[l + 3] = cs[l + 6]
                    cs[l + 3] = cs[l + 7]
                    cs[l + 5] = cs[l + 8]
                    
                    cs[l + 6] = tempA
                    cs[l + 7] = tempB
                    cs[l + 8] = tempC
                    
                    fi_solution = copy.deepcopy(cs)
                    break
                
    
    distance = findEclidianDistance(iterations, fi_solution)
    
    return odist, distance, fi_solutio

# display colours
#plot_colours(colours, permutation)
# to save image, use save button in window

returnSol1 = firstImpovementHillClimb(100)

# print "Original colours: R / G / B "
# print red
# print green
# print blue
#  
# print "        "

# solution = sol(red, green, blue)
# print solution
# 
# for i in range(3000):
#     print "Iteration : ", i, " " , (solution[i])
# 
# print "        "
 
odist1, distance1, soln1 = firstImpovementHillClimb()
print "First Improvement Hill Climb:"
print "Original Distance: " , odist1
print "Improved Distance:" , distance1
print "Improvement: ", (odist1 - distance1)
 
print "        "
 
odist2, distance2, soln2 = firstImpovementHillClimbImproved()
print "First Improvement Hill Climb v2:"
print "Original Distance: " , odist2
print "Improved Distance:" , distance2
print "Improvement: ", (odist2 - distance2)





# for i in range(50):
#     print "RED:", soln[i], ", GREEN: ", soln[i+1], ", BLUE:" ,soln[i+2]
#      
# print "        "
# 
# total = 0
#  
# for i in range(999):
#      
#     print "        "
#      
#     distance = findDistance(red[i],green[i],blue[i],red[i+1],green[i+1],blue[i+1])
#     print "Test Distance", distance
#      
#     total = total + distance
#      
#     print "Total distance", total
#     
#     print "Iteration:", i

