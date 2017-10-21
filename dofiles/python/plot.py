import matplotlib  
matplotlib.use('Agg')
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter


fig = plt.figure()
ax = Axes3D(fig)
#ax.view_init(elev=10., azim=30)

dataSize = [64, 128, 256, 512, 1000]
epochNum = [10, 20, 40, 80]

X, Y = np.meshgrid(epochNum, dataSize)
data = np.load("./result/resultGP.npz")
retGP = data["retGP"]
ax.plot_surface(X, Y, retGP, rstride=32, cstride=10, color='r', label="simple graphial password")

data = np.load("./result/resultGPpro.npz")
retGPpro = data["retGPpro"]
ax.plot_surface(X, Y, retGPpro, rstride=32, cstride=10, color='g', label="advanced graphical password")

ax.set_xlabel('Epoch number')
ax.set_ylabel('Training set size')
ax.set_zlabel('Precision')

# ax.set_zlim(0., 1.0)
# ax.zaxis.set_major_locator(LinearLocator(10))  
plt.savefig("test.jpg")
