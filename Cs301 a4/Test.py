import numpy as np
import time
import matplotlib.pyplot as plt

np.random.seed(0)


def Shortestpath(B, T, TT, n, Matrix):
    for l in range(n):
        for i in range(n):
            for j in range(n):
                B[i][j] = min(
                    B[i][j], T[i][l] + B[l][j] + TT[l], B[i][l] + B[l][j]
                )  # bus transportation
                T[i][j] = min(
                    T[i][j], B[i][l] + T[l][j] + TT[l], T[i][l] + T[l][j]
                )  # train transportation
                Matrix[i][j] = min(T[i][j], B[i][j])

    print(Matrix[0])


# functional test
# zero city
#B = [[]]
#T = [[]]
#TT = []

#just bus station by makeing train matrix infinity
#INF = 999999999
#m5b=np.random.randint(0,200,size=(5,5))
#for i in range(5):
#    m5b[i][i]=0
#B = list(map(list, m5b))
#
#T = [[INF, INF, INF, INF, INF],
#    [INF, INF, INF, INF, INF],
#    [INF, INF, INF, INF, INF],
#    [INF, INF, INF, INF, INF],
#    [INF, INF, INF, INF, INF]]
#
#TT = [INF, INF, INF, INF, INF]


#10 city random matrix
#m10b=np.random.randint(0,200,size=(10,10))
#for i in range(10):
#    m10b[i][i]=0
#B = list(map(list, m10b))
#
#print("Bus matrix",B)
#
#m10t=np.random.randint(0,200,size=(10,10))
#for i in range(10):
#    m10t[i][i]=0
#T = list(map(list, m10t))
#print("Train matrix",B)
#
#
#
#TT = np.random.randint(0,200,size=(10)) 
#TT = list(map(int, TT))


#100 city random matrix
#m100b=np.random.randint(0,200,size=(100,100))
#for i in range(100):
#    m100b[i][i]=0
#B = list(map(list, m100b))
#
#print("Bus matrix",B)
#
#m100t=np.random.randint(0,200,size=(100,100))
#for i in range(100):
#    m100t[i][i]=0
#T = list(map(list, m100t))
#print("Train matrix",B)
#
#TT = np.random.randint(0,200,size=(100)) 
#TT = list(map(int, TT))


#all cost is zero 
#B = [[0, 0, 0, 0, 0],
#    [0, 0, 0, 0, 0],
#    [0, 0, 0, 0, 0],
#    [0, 0, 0, 0, 0],
#    [0, 0, 0, 0, 0]]
#
#T = [[0, 0, 0, 0, 0],
#    [0, 0, 0, 0, 0],
#    [0, 0, 0, 0, 0],
#    [0, 0, 0, 0, 0],
#    [0, 0, 0, 0, 0]]
#
#TT = [0, 0, 0, 0, 0]

#all cost is infinity
INF = 999999999
#B = [[INF, INF, INF, INF, INF],
#    [INF, INF, INF, INF, INF],
#    [INF, INF, INF, INF, INF],
#    [INF, INF, INF, INF, INF],
#    [INF, INF, INF, INF, INF]]
#
#T = [[INF, INF, INF, INF, INF],
#    [INF, INF, INF, INF, INF],
#    [INF, INF, INF, INF, INF],
#    [INF, INF, INF, INF, INF],
#    [INF, INF, INF, INF, INF]]
#
#TT = [INF, INF, INF, INF, INF]


print("Travel time between stations", TT)


Matrix = list(map(list, B))  # Matrix is a list of lists. For populate matrix we can use either B or T

Matrix = np.array(Matrix)

start = time.time()

Shortestpath(B, T, TT, 5, Matrix)

end = time.time()

print(end - start)
