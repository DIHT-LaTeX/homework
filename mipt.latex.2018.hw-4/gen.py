import numpy as np

SIZE = 100
A = np.pi
B = np.exp(1)
err = np.random.normal(scale=np.pi, size=SIZE)
f = lambda x: A * x + B

x = np.linspace(-10, 10, SIZE)
y = f(x) + err
a, b = np.polyfit(x, y, deg = 1)
print(a, ' ', b, end='\n')
    
f = open("data.dat", "w")
f.write("x\ty")

for i in range(len(x)):
	f.write("\n{}\t{}".format(x[i], y[i]))