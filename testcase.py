import mumpy as np

numdata=180
x=.5-np.random.random(numdata)*1.
y=.5-np.random.random(numdata)*1.
z=-1 +x -2*y**3 +3*x**2 -4*x*y**2 +5*y*x**3 +6*x*y**5 -7*x**5#+np.random.random(numdata)*0.05
m=reducedpolyfit2D(x,y,z,ord=5)
nx,ny=100,100
xx,yy=np.meshgrid(np.linspace(x.min(),x.max(),nx),np.linspace(y.min(),y.max(),ny))
zz=reducedpolyval2D(xx,yy,m)

#plotting
from matplotlib import pyplot as plt
plt.imshow(zz,extent=(x.min(),y.max(),x.max(),y.min()))
plt.scatter(x,y,c=z)
plt.show()
