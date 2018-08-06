# This script requires a couple of libraries to be installed and loaded
import matplotlib.pyplot as plt
import numpy as np
import math
import os
import copy
import random as rnd
import numpy as np
import time
from numpy import median

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

size = 1000; # number of colours

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
    
#Swaps two colours in a given list
def swap(inSol, low, high):
    
    sol = list(inSol)
    sol[low], sol[high] = sol[high], sol[low]
    return sol

#calculates the euclidian distance of an entire list
def evaluate(sol):
    
    totalSum = 0
    distance = 0
 
    for i in range(size - 1):
        
        X1 = col[sol[i]][0]
        Y1 = col[sol[i]][1]
        Z1 = col[sol[i]][2]
     
        X2 = col[sol[i+1]][0]
        Y2 = col[sol[i+1]][1]
        Z2 = col[sol[i+1]][2]
 
        varA = np.power((X2 - X1),2)
        varB = np.power((Y2 - Y1),2)
        varC = np.power((Z2 - Z1),2)
        
        totalSum = varA + varB + varC
        
        runningTotal = math.sqrt(totalSum)
        
        distance += runningTotal
 
    return distance

#calculates the euclidian distance between two colours
def findDistance(sol, i, x):
    
    totalSum = 0
    distance = 0
        
    X1 = col[sol[i]][0]
    Y1 = col[sol[i]][1]
    Z1 = col[sol[i]][2]
    
    X2 = col[sol[x]][0]
    Y2 = col[sol[x]][1]
    Z2 = col[sol[x]][2]
    
    varA = np.power((X2 - X1),2)
    varB = np.power((Y2 - Y1),2)
    varC = np.power((Z2 - Z1),2)
    
    totalSum = varA + varB + varC
    
    runningTotal = math.sqrt(totalSum)
    
    distance += runningTotal
 
    return distance
     
objVal1 = [] # Hill Climber
# Solution for first improvement hill climb
def firstImpovementHillClimb(iter, sol):
    print "First Improvement Hill Climb running... \n"
    start_time = time.time()
    count = 1
    solution = sol
    curSol = list(solution)
    fiSol = list(solution)
    odist = evaluate(solution)
    for i in range(iter):
        R1 = rnd.randint(0,size-1) 
        R2 = rnd.randint(0,size-1)
        #print curSol
        newSol = swap(curSol, R1, R2)
        dist = evaluate(newSol)
        if evaluate(newSol)<evaluate(curSol):
            curSol = newSol
            fdist = evaluate(curSol)
            ##print "SWAP # ", count, "\t", "[ PREVIOUS DISTANCE: ", evaluate(curSol) , "] \t [", "NEW DISTANCE: ", evaluate(newSol) , "]"
            count += 1
            objVal1.append(evaluate(curSol))
    ##print ""
    print("--- %s seconds ---" % (time.time() - start_time))
    return odist, fdist, fiSol


# Solution for first improvement hill climb improved
def firstImpovementHillClimbv2(iter, sol):
    objVal2 = [] # Hill Climber v2
    print "First Improvement Hill Climb v2 running... \n"
    start_time = time.time()
    count = 1
    solution = sol
    curSol = list(solution)
    fiSol = list(solution)
    odist = evaluate(solution)
    for i in range(iter):
        R1 = rnd.randint(0,size-1) 
        R2 = rnd.randint(0,size-1)
        R3 = rnd.randint(0,size-1) 
        R4 = rnd.randint(0,size-1)
        newSol2 = swap(curSol, R1, R2)
        newSol = swap(newSol2, R3, R4)
        dist = evaluate(newSol)
        if evaluate(newSol)<evaluate(curSol):
            curSol = newSol
            fdist = evaluate(curSol)
            ##print "SWAP # ", count, "\t", "[ PREVIOUS DISTANCE: ", evaluate(curSol) , "] \t [", "NEW DISTANCE: ", evaluate(newSol) , "]"
            count += 1
            objVal2.append(evaluate(curSol))
    ##print ""
    rt = ((time.time() - start_time))
    print("--- %s seconds ---" % (time.time() - start_time))
    return odist, fdist, fiSol, objVal2,rt


def jamiesAlgotithm(iter, sol):  
    objVal3 = [] # Custom Algorithm
    print "My Custom Algoithm Running... \n"
    start_time = time.time()
    count = 1
    solution = sol 
    curSol = list(solution)
    fiSol = list(solution)
    odist = evaluate(solution)
    count = 0 

#To improve results, iterate multiple times
    for i in range (iter):
        for x in range(size - 2):       
            solu = findDistance(curSol, x, x+1)
            soln = findDistance(curSol, x, x+2)
            if (soln < solu):
                newSol = swap(curSol, x+1, x+2)
                count += 1
                #print "SWAP # ", count , "Improvement" , (solu - soln), "New Distance:", evaluate(curSol)
                curSol = copy.deepcopy(newSol)
                objVal3.append(evaluate(curSol))
        fiSol = copy.deepcopy(curSol)
        fdist = evaluate(fiSol)
    #print ""
    rt = (time.time() - start_time)
    print("--- %s seconds ---" % (time.time() - start_time))
    return odist, fdist, fiSol, objVal3,rt

# display colours
#plot_colours(colours, permutation)
# to save image, use save button in window

#ensures that col is the same size as the current list in order to plot properly
colors = []
for i in range(size):
    colors.append(col[i])

solution = permutation[:]
rnd.shuffle(solution)
odist1, fdist1, soln1 = firstImpovementHillClimb(100, solution)
    
   
print "Original Distance: " , odist1
print "Improved Distance:" , fdist1
print "Improvement : " , (odist1 - fdist1)
print "Objective Function Values: ", objVal1
  
#Used to plot solutions for firstImpovementHillClimb
# plot_colours(colors, solution)
# plot_colours(colors, soln1)
# plt.plot(objVal1)
# plt.show()
  
print "        "
  
new_solution1 = permutation[:]
rnd.shuffle(new_solution1)
odist2, fdist2, soln2,objVal2,rt = firstImpovementHillClimbv2(100, new_solution1)
    
print "Original Distance: " , odist2
print "Improved Distance:" , fdist2
print "Improvement : " , (odist2 - fdist2)
print "Objective Function Values: ", objVal2
    
    
print "        "
  
#Used to plot solutions for firstImpovementHillClimbv2
# plot_colours(colors, new_solution1)
# plot_colours(colors, soln2)
# plt.plot(objVal2)
# plt.show()
   
new_solution2 = permutation[:]
rnd.shuffle(new_solution2)
odist3, fdist3, soln3, objVal3,rt = jamiesAlgotithm(1, new_solution2)
    
print "Original Distance: " , odist3
print "Improved Distance:" , fdist3
print "Improvement : " , (odist3 - fdist3)
print "Objective Function Values: ", objVal3
  
  
print "        "

# Used to plot solutions for my custom algorithm
# plot_colours(colors, new_solution2)
# plot_colours(colors, soln3)
# plt.plot(objVal3)
# plt.show()

# print "Plotted Successfully"


# Used for iterating 20 times to find mean, median and std deviation 
# total = 0
# average = 0
# iterations = 20
# all = []
# bestImp = 0
# bestImpr = []
# objVal = []
# improvement = 0
# runTime = 0
#   
# for i in range(iterations):
#     print "Iteration #" , (i+1) ,": Running..."
#     new_solution3 = permutation[:]
#     #rnd.shuffle(new_solution3)
#     odist4, fdist4, soln4, objVal3,rt = firstImpovementHillClimbv2(100, new_solution3)
#     if (improvement > bestImp):
#         bestImp = improvement
#         best_Impr = copy.deepcopy(soln4)
#         objVal = objVal3
#         bestSol = soln4
#         runTime = rt
#     improvement = (odist4 - fdist4)
#     total = total + improvement
#     average = total / (i+1)
#     all.append(improvement)
#     print "Average Original Distance:" 
#     print "Original Distance: " , odist4
#     print "Improved Distance:" , fdist4
#     print "Improvement : " , (odist4 - fdist4)
#     print "Running Total: " , total
#     print "Current Average: " , average
#     print "        "
#     print "        "
#  
# average = total / iterations
#  
# for i in range(iterations):
#     if (i == iterations -2):
#         break
#  
#     if (all[i+1] < all[i+2]):
#         swap(all,i+1,i+2)
#  
# x = (len(all) / 2)
#  
# median = all[x]
#  
# current = 0
# for i in range(iterations):
#     current = all[i]
#     current = current - average
#     stdDeviation = np.power(current,2)
#  
# print "Total Improvement: " , total
# print "Average Improvement: " , average
# print "Median Average: ", median
# print "Standard Deviation: ", stdDeviation
# print "Run Time: ", runTime

# Plot best solution
# plot_colours(colors, new_solution3)
# plot_colours(colors, bestSol)
# plt.plot(objVal)
# plt.show()


