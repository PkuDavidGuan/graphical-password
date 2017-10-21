from nnPIN import modelPIN
from nnText import modelText
from nnGP import modelGP
from nnGPpro import modelGPpro
import numpy as np

dataSize = [64, 128, 256, 512, 1000]
epochNum = [10, 20, 40, 80, 100, 120]
hiddenLayerSize = [8, 16, 32]

retGP = np.zeros([len(dataSize), len(epochNum), len(hiddenLayerSize)])
retGPpro = np.zeros([len(dataSize), len(epochNum), len(hiddenLayerSize)])
'''
for i in range(0, len(dataSize)):
    for j in range(0, len(epochNum)):
        for k in range(0, len(hiddenLayerSize)):
            retGP[i, j, k] = modelGP(dataSize[i], epochNum[j], hiddenLayerSize[k])
np.savez("./result/resultLab2GP.npz", retGP=retGP)
'''

for i in range(0, len(dataSize)):
    for j in range(0, len(epochNum)):
        for k in range(0, len(hiddenLayerSize)):
            retGPpro[i, j, k] = modelGPpro(dataSize[i], epochNum[j], hiddenLayerSize[k])
np.savez("./result/resultLab2GPpro.npz", retGPpro=retGPpro)