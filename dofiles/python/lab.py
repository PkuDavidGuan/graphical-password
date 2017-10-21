from nnPIN import modelPIN
from nnText import modelText
from nnGP import modelGP
from nnGPpro import modelGPpro
import numpy as np

dataSize = [64, 128, 256, 512, 1000]
epochNum = [10, 20, 40, 80, 100, 120]
retPIN = np.zeros([len(dataSize), len(epochNum)])
retText = np.zeros([len(dataSize), len(epochNum)])
retGP = np.zeros([len(dataSize), len(epochNum)])
retGPpro = np.zeros([len(dataSize), len(epochNum)])

'''
for i in range(0, 5):
    for j in range(0, 4):
        retPIN[i, j] = modelPIN(dataSize[i], epochNum[j])
np.savez("./result/resultPIN.npz", retPIN=retPIN)


for i in range(0, 1):
    for j in range(0, 1):
        retText[i, j] = modelText(dataSize[i], epochNum[j])
np.savez("./result/resultText.npz", retText=retText)


for i in range(0, len(dataSize)):
    for j in range(0, len(epochNum)):
        retGP[i, j] = modelGP(dataSize[i], epochNum[j], 32)
np.savez("./result/resultGP.npz", retGP=retGP)
'''

for i in range(0, len(dataSize)):
    for j in range(0, len(epochNum)):
        retGPpro[i, j] = modelGPpro(dataSize[i], epochNum[j], 32)
np.savez("./result/resultGPpro.npz", retGPpro=retGPpro)