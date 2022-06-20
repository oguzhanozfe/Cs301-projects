import time
from statistics import mean
import statistics 
import numpy as np

def lcs(X,Y,i,j):
    if (i == 0 or j == 0):
        return 0
    elif X[i-1] == Y[j-1]:
        return 1 + lcs(X,Y,i-1,j-1)
    else:
        return max(lcs(X,Y,i,j-1),lcs(X,Y,i-1,j))

f = open("5dna.txt", "r")
mylist = f.readlines()
timelist5 = []
counter = 0
while(len(mylist) > 0):
    X = mylist.pop(0)
    Y = mylist.pop(0)
    start_time = time.time()
    print(lcs(X,Y,len(X),len(Y)))
    end_time = time.time()
    print('Time: ', end_time - start_time)
    timelist5.append(end_time - start_time)
    counter = counter + 1
f.close()

print('Average time of 25: ', statistics.fmean(timelist5))
print('Standard deviation of 5: ', statistics.stdev(timelist5))

f = open("10dna.txt", "r")
mylist = f.readlines()
timelist10 = []
counter = 0
while(len(mylist) > 0):
    X = mylist.pop(0)
    Y = mylist.pop(0)
    start_time = time.time()
    print(lcs(X,Y,len(X),len(Y)))
    end_time = time.time()
    print('Time: ', end_time - start_time)
    timelist10.append(end_time - start_time)
    counter = counter + 1
f.close()

print('Average time of 10: ', statistics.fmean(timelist10))
print('Standard deviation of 10: ', statistics.stdev(timelist10))

f = open("15dna.txt", "r")
mylist = f.readlines()
timelist15 = []
counter = 0
while(len(mylist) > 0):
    X = mylist.pop(0)
    Y = mylist.pop(0)
    start_time = time.time()
    print(lcs(X,Y,len(X),len(Y)))
    end_time = time.time()
    print('Time: ', end_time - start_time)
    timelist15.append(end_time - start_time)
    counter = counter + 1
f.close()

print('Average time of 15: ', statistics.fmean(timelist15))
print('Standard deviation of 15: ', statistics.stdev(timelist15))

f = open("20dna.txt", "r")
mylist = f.readlines()
timelist20 = []
counter = 0
while(len(mylist) > 0):
    X = mylist.pop(0)
    Y = mylist.pop(0)
    start_time = time.time()
    print(lcs(X,Y,len(X),len(Y)))
    end_time = time.time()
    print('Time: ', end_time - start_time)
    timelist20.append(end_time - start_time)
    counter = counter + 1
f.close()

print('Average time of 20: ', statistics.fmean(timelist20))
print('Standard deviation of 20: ', statistics.stdev(timelist20))

f = open("25dna.txt", "r")
mylist = f.readlines()
timelist25 = []
counter = 0
while(len(mylist) > 0):
    X = mylist.pop(0)
    Y = mylist.pop(0)
    start_time = time.time()
    print(lcs(X,Y,len(X),len(Y)))
    end_time = time.time()
    print('Time: ', end_time - start_time)
    timelist25.append(end_time - start_time)
    counter = counter + 1
f.close()

print('Average time of 25: ', statistics.fmean(timelist25))
print('Standard deviation of 25: ', statistics.stdev(timelist25))