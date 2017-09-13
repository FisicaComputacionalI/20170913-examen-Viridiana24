import numpy as np
import pylab as plt
periodo=2
X=np.linspace(2016,2017)
Y = np.sin(2*np.pi*X/periodo)
amplitud=3
plt.plot(X,Y)
plt.title("Anios en la Universidad")
plt.xlabel("Anio de ingreso")
plt.ylabel("Tiempo en la universidad")
plt.grid(True)
plt.axis('tight')
plt.plot(X, Y, color="turquoise", linewidth=1.2, linestyle="-",label="f(x)=sinx")
plt.plot(label="f(x)=sin")
plt.legend()
plt.savefig('graph.png')
plt.show()
