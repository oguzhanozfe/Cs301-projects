import numpy as np
import time
import matplotlib.pyplot as plt


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


# for creation of random matrix
m400b=np.random.randint(0,200,size=(400,400))
for i in range(400):
    m400b[i][i]=0
B = list(map(list, m400b))

print("Bus matrix",B)

m400t=np.random.randint(0,200,size=(400,400))
for i in range(400):
    m400t[i][i]=0
T = list(map(list, m400t))
print("Train matrix",B)



TT = np.random.randint(0,200,size=(400)) 
TT = list(map(int, TT))

print("Travel time between stations",TT)


Matrix = list(map(list, B))  # Matrix is a list of lists. For populate matrix we can use either B or T

Matrix = np.array(Matrix)

start = time.time()

Shortestpath(B, T, TT, 400, Matrix)

end = time.time()

print(end - start)
