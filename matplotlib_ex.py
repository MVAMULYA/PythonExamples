#!usr/bin/python

import numpy as np 
import matplotlib.pyplot as plt

x = np.linspace(0,20,100)
y1 = np.cos(x)
y2 = np.sin(x)

plt.plot(x , y1, "-g",label="cosine")
plt.plot(x , y2, "-b",label= "sine")

plt.legend(loc= "upper right")

plt.ylim(-1.5,1.5)
plt.show()