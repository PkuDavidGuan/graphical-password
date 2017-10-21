import numpy as np
from sklearn.preprocessing import OneHotEncoder

traceNum = 10
iterNum = 1024
gridNum = 9
maxNum = 2

for i in range(0, traceNum):
    password = np.random.rand(1, gridNum)
    for j in range(0, password.shape[1]):
        if password[0, j] < 0.5:
            password[0, j] = 0
        else:
            password[0, j] = 1

    x = np.zeros([iterNum, gridNum])
    y = np.zeros([iterNum, 1])
    
    for j in range(0, iterNum):
        input = np.floor(np.random.rand(1, gridNum) * (maxNum + 1))
        output = np.matmul(input, np.transpose(password))
        x[j] = input
        y[j] = output
    
    fileName = "./traces/GPpro" + str(i) + ".npz"
    np.savez(fileName, x=x, y=y)