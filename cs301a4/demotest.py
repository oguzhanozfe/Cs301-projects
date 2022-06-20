import numpy as np
import time
import matplotlib.pyplot as plt
inf = 999999999

def Shortestpath(B, T, TT, n, Matrix):
    for l in range(n):
        for i in range(n):
            for j in range(n):
                B[i][j] = min( B[i][j], T[i][l] + B[l][j] + TT[l], B[i][l] + B[l][j])  # bus transportation
                T[i][j] = min(T[i][j], B[i][l] + T[l][j] + TT[l], T[i][l] + T[l][j])  # train transportation
                Matrix[i][j] = min(T[i][j], B[i][j])

    print(Matrix[0])


#input 1

#B=[[0,20,inf,inf,inf,inf,inf],
#  [20,0,20,inf,inf,40,inf],
#  [inf,20,0,15,inf,inf,inf],
#  [inf,inf,15,0,inf,inf,10],
#  [inf,inf,inf,inf,0,inf,inf],
#  [inf,40,inf,10,inf,0,inf],
#  [inf,inf,inf,10,inf,inf,0]]
#
#T=[[0,10,inf,inf,20,inf,inf],
#  [10,0,inf,inf,5,inf,inf],
#  [inf,inf,0,inf,inf,inf,inf],
#  [inf,inf,inf,0,inf,inf,inf],
#  [20,5,inf,inf,0,10,inf],
#  [inf,inf,inf,inf,inf,0,30],
#  [inf,inf,inf,inf,inf,30,0]]
#
#TT = [5,10,inf,inf,inf,10,10]

#input 2
#TT =[5,5,25,inf,inf,10]
#
#B=[[0,40,inf,inf,inf,inf],
#  [40,0,5,inf,inf,inf],
#  [inf,5,0,inf,5,inf],
#  [inf,inf,inf,0,inf,inf],
#  [inf,inf,5,inf,0,5],
#  [inf,inf,inf,inf,5,0]]
#
#T=[[0,  inf,    10, inf,    inf,    inf ],
#  [inf, 0,  inf,    5,  inf,    inf],
#  [10,  inf,    0,  5,    inf,    inf],
#  [inf, 5,  5,  0,  inf,    40],
#  [inf, inf ,inf,   inf,    0,  inf],
#  [inf, inf,    inf,    40, inf,    0]]

#input 3

#TT=[5,inf,10,inf,inf]
#
#B = [[0,30,30,inf,inf],
#    [30,0,20,22,inf],
#    [30,20,0,20,inf],
#    [inf,22,20,0,inf],
#    [inf,inf,inf,inf,0]]
#
#T=  [[0,inf,20,inf,75],
#    [inf,0,inf,inf,inf],
#    [20,inf,0,inf,40],
#    [inf,inf,inf,0,inf],
#    [75,inf,40,inf,0]]

#input 4

#TT=[inf,4,inf,7,inf,8]
#
#B= [[0,inf,23,27,inf,inf],
#   [inf,0,18,13,inf,inf],
#   [23,18,0,inf,inf,17],
#   [27,13,inf,0,inf,20],
#   [inf,inf,inf,inf,0,inf],
#   [inf,inf,17,20,inf,0]]
#
#T= [[0,inf,inf,inf,inf,inf],
#   [inf,0,inf,inf,inf,11],
#   [inf,inf,0,inf,inf,inf],
#   [inf,inf,inf,0,12,22],
#   [inf,inf,inf,12,0,17],
#   [inf,11,inf,22,17,0]]





Matrix = list(map(list, B))  # Matrix is a list of lists. For populate matrix we can use either B or T

Matrix = np.array(Matrix)

start = time.time()

Shortestpath(B, T, TT, 6, Matrix)

end = time.time()

print(end - start)
