#! /usr/bin/env python3

import matplotlib.pyplot as plt
import random
import math

# Creating a figure instance to write to pdf later
f = plt.figure()

# Plotting so axes are same scale
# Zooming in on majority of data points, losing
# a few outliers though. (To get full scale
# including outliers, plot on (0, 4) for
# both axes. 
plt.ylim(0, 2.5)
plt.xlim(0, 2.5)


# Use final_data.txt to generate my x and y coordinates
# x = budget increase
# y = voter increase
# N = length

x = []
y = []
dist = []
areas = []

data = open("final_data.txt", "rt")
line = data.readline() # reading header
line = data.readline() # reading real first line
while line:
    parts = line.split("|")

    # Getting rid of trailing white space
    budgetInc = float(parts[2].rstrip())
    voterInc = float(parts[1].rstrip())
    curDist = parts[0].rstrip()
    circleSize = int(parts[3])

    dist.append(curDist)
    x.append(budgetInc)
    y.append(voterInc)
    areas.append(circleSize)

    line = data.readline()

N = len(x)

# TEST CODE - when run, matches final_data.txt
# for i in range(0, N):
#    print("x = " + str(x[i]) + ". y = " + str(y[i]))

# Making a list of colors
colors = [random.random() for i in range(N)]

# Make a list of circle sizes
# LATER - somehow based on census data?
areas = [areas[i]*0.1 for i in range(len(areas))]

# Make the scatter plot
plt.scatter(x, y, c = colors, s = areas, alpha = 0.5)

# spacing out the ticks - didn't work!
# plt.margins(0.9)
# plt.subplots_adjust(bottom=0.15)

# WANT TO LABEL EACH INDIV CIRCLE WITH THE DISTRICT
# use district list
           
# Specify the labels
plt.xlabel("Percent budget increase from 2000 to 2004")
plt.ylabel("Percent voter increase from 2004 to 2008")

# Save the plot to a PDF file
f.savefig("graph.pdf")

data.close()
