import numpy as np
from sklearn.preprocessing import OneHotEncoder

traceNum = 10
iterNum = 1024

for i in range(0, traceNum):
    password = np.random.rand(1,4)
    password = np.floor(password*10)
    x = np.zeros([iterNum,40])
    y = np.zeros([iterNum,4,10])

    input = np.zeros([1,40])
    output = np.zeros([4,10])
    for j in range(0,4):
        input[0, int(password[0,j])+j*10] = 1
        output[j, int(password[0,j])] = 1
    
    for j in range(0, iterNum):
        x[j] = input
        y[j] = output
    
    fileName = "./traces/PIN" + str(i) + ".npz"
    np.savez(fileName, x=x, y=y)