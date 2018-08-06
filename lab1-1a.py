#import matplotlib.pyplot as plt
import random as rnd

x = range(100) # Integer numbers from 0 to 99 in sequence
y = range(100) # Integer numbers from 0 to 99 in sequence
#plt.plot(x,y) # plot x and y with default line style and color (solid blue)
#plt.ylabel('consecutive numbers') # Sets a label for the y axis
#plt.figure() # creates a figure window
#plt.show() # shows the plot

print x
print y

print

y1 = range(100)

for i in range(0, 99):
    y1[i] = rnd.randint(0,100)
print y1

#plt.plot(x, y1)
#plt.ylabel('consecutive numbers')
#plt.figure()
#plt.show()

#plt.plot(x,y1,'ro')
#plt.ylabel('consecutive numbers')
#plt.figure()
#plt.show()