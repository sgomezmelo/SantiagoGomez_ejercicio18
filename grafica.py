import matplotlib.pyplot as plt
import numpy as np

datos = np.loadtxt('edo.txt')
x = datos[:,0]
y = datos[:,1]
y2 = np.exp(-x)

plt.figure()
plt.scatter(x,y)
plt.plot(x,y2)
plt.savefig('EcDif.pdf')
