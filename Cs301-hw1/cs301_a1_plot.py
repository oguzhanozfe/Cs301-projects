import matplotlib.pyplot as plt
import numpy as np

w=0.4

time = np.array([5, 10, 15, 20, 25])
naive = np.array([0.0003075000000000161  ,  0.00040049999999997    , 0.0004997253417968    ,  0.000500679016113,  0.00050091743469  ])

plt.bar(time, naive, width=w, label='Naive')
#plt.bar(time+w, memo, width=w, label='Memoization')
plt.xticks(time+w/2, ('5', '10', '15', '20','25'))
plt.legend()



plt.xlabel("Length of DNA")
plt.ylabel("Average Time (s)")
plt.title("Average Time vs Length of Worst case string")

plt.show()
