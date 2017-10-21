import matplotlib  
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt
dataSize = [64, 128, 256, 512, 1000]
retText = [1., 1., 1., 1., 1.]
data = np.load("./result/resultLab2GP.npz")
retGP = data["retGP"]

plt.plot(dataSize, retGP[:,4, 2], '-', label = "PassFaces")
data = np.load("./result/resultLab2GPpro.npz")
retGP = data["retGPpro"]
plt.plot(dataSize, retGP[:,4, 2], '-.', label = "GrIDsure")
plt.plot(dataSize, retText, '--', label = "PIN/text")
# p = plt.axhspan(0.9, 0.98, facecolor='0.5', alpha=0.5)
plt.axhline(y=0.9, color='r')
plt.legend(loc='lower right')
plt.xlabel("Training set size")
plt.ylabel("Precision rate")
plt.savefig("line.eps")

epochNum = [10, 20, 40, 80, 100, 120]