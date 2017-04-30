import csv
import json
import sys


f = open(sys.argv[1], 'r')

counter = 0

data = [[],[]]

for line in f:
    print line
    if counter != 0:
        points = line.split(',')
        data[0].append(points[0])
        data[1].append(float(points[1]))

print data
        
            
