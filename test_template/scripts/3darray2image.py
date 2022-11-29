import numpy as np 
import matplotlib.pyplot as plt

rgb = np.array([[[255,0,0],[0,0,0],[0,128,128]]])

print("red",rgb[0][0])
print("blue",rgb[0][1])
print("green",rgb[0][2])
print("shape", rgb.shape)
plt.imshow(rgb)
plt.show()

