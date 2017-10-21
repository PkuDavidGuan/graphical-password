import numpy as np
import random

traceNum = 10
iterNum = 1024
picNum = 100
pickedPicNum = 5
panelPicNum = 9

for i in range(0, traceNum):
    rank = np.random.permutation(picNum)
    password = np.zeros([1, picNum])
    for j in range(0, pickedPicNum):
        password[0, int(rank[j])] = 1

    x = np.zeros([iterNum, picNum])
    y = np.zeros([iterNum, 1, picNum])
    
    for j in range(0, iterNum):
        luckydog = random.randint(1, pickedPicNum) - 1
        input = np.zeros([1, picNum])
        output = np.zeros([1, picNum])
        input[0, int(rank[luckydog])] = 1
        output[0, int(rank[luckydog])] = 1

        count = 1
        while count < panelPicNum:
            luckydog = random.randint(1, picNum) - 1
            #print luckydog
            #print input[0, luckydog]
            #print password[0, luckydog]
            #print "\n"
            if input[0, luckydog]==0 and password[0, luckydog]==0:
                input[0, luckydog] = 1
                count = count + 1 

        x[j] = input
        y[j] = output
    
    #print password
    #print x
    #print y
    fileName = "./traces/GP" + str(i) + ".npz"
    np.savez(fileName, x=x, y=y)