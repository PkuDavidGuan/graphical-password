import matplotlib  
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt
dataSize = [64, 128, 256, 512, 1000]
retText = [1., 1., 1., 1., 1.]

data = np.load("./result/resultLab2GP.npz")
retGP = data["retGP"]
plt.subplot(121)
plt.plot(dataSize, retGP[:,4, 0], '-', label = "8 hidden units")
plt.plot(dataSize, retGP[:,4, 1], '-.', label = "16 hidden units")
plt.plot(dataSize, retGP[:,4, 2], '--', label = "32 hidden units")

# plt.legend(loc='upper right')
plt.xlabel("Training set size")
plt.ylabel("Precision rate")
plt.title("PassFaces")


data = np.load("./result/resultLab2GPpro.npz")
retGP = data["retGPpro"]
plt.subplot(122)
plt.plot(dataSize, retGP[:,4, 0], '-', label = "8 hidden units")
plt.plot(dataSize, retGP[:,4, 1], '-.', label = "16 hidden units")
plt.plot(dataSize, retGP[:,4, 2], '--', label = "32 hidden units")

# plt.legend(loc='upper right')
plt.xlabel("Training set size")
plt.ylabel("Precision rate")
plt.title("GrIDsure")

plt.savefig("line2.eps")
