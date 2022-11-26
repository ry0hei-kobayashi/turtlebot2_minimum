import numpy as np 
import matplotlib.pyplot as plt

array = np.array([[0,64,172,255]])
print("shape",array.shape)
plt.imshow(array, cmap="gray")
plt.show()
