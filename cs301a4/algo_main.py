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
m100b = np.random.randint(0, 200, size=(100, 100))
for i in range(100):
    m100b[i][i] = 0
B = list(map(list, m100b))

print("Bus matrix", B)

m100t = np.random.randint(0, 200, size=(100, 100))
for i in range(100):
    m100t[i][i] = 0
T = list(map(list, m100t))
print("Train matrix", B)


TT = np.random.randint(0, 200, size=(100))
TT = list(map(int, TT))

print("Travel time between stations", TT)


Matrix = list(
    map(list, B)
)  # Matrix is a list of lists. For populate matrix we can use either B or T

Matrix = np.array(Matrix)

start = time.time()

Shortestpath(B, T, TT, 100, Matrix)

end = time.time()

print(end - start)
