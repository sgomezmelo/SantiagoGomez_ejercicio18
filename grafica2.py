import matplotlib.pyplot as plt
import numpy as np

datos = np.loadtxt('edo2.txt')
x = datos[:,0]
y = datos[:,1]
dy = datos[:,2]
y2 = np.cos(x)

plt.figure()
plt.scatter(x,y, label = 'Numerico')
plt.plot(x,y2, label = 'Analitico')
plt.legend()
plt.savefig('EcDif2.pdf')

plt.figure()
plt.scatter(dy,y)
plt.savefig('zy.png')
