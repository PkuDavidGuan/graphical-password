import numpy as np
import random

traceNum = 10
iterNum = 1024

for i in range(0, traceNum):
    password = np.random.rand(1, 12)
    password = np.floor(password * 94) + 1
    passwordLen = random.randint(1, 12)
    for j in range(passwordLen, 12):
        password[0, j] = 0
    
    x = np.zeros([iterNum, 12*95])
    y = np.zeros([iterNum, 12, 95])
    input = np.zeros([1,12*95])
    output = np.zeros([12,95])
    for j in range(0,12):
        input[0, int(password[0,j])+j*95] = 1
        output[j, int(password[0,j])] = 1

    for j in range(0, iterNum):
        x[j] = input
        y[j] = output
    
    fileName = "./traces/text" + str(i) + ".npz"
    np.savez(fileName, x=x, y=y)