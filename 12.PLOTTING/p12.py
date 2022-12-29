#Practice
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits import mplot3d
from math import pi,sin,cos,exp
from mpl_toolkits import mplot3d
"""plt.figure(figsize=(10,6))
x = np.linspace(-5,5, 100)
plt.plot(x, x**2,"gd",label="test")
plt.title(f"Plot of Various Polynomials from {x[0]} to{x[-1]}")
plt.xlabel("X axis", fontsize = 18)
plt.ylabel("Y axis", fontsize = 18)
plt.legend(loc = 2)
plt.xlim(-6.6)
plt.ylim(0,30)
plt.grid()
plt.show()"""
#subplots
"""
x = np.arange(11)
y = x**2
plt.figure(figsize = (14, 8))
plt.subplot(2, 3, 1)
plt.plot(x,y)
plt.title("Plot")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid()
plt.subplot(2, 3, 2)
plt.scatter(x,y)
plt.title("Scatter")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid()
plt.subplot(2, 3, 3)
plt.bar(x,y)
plt.title("Bar")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid()
plt.subplot(2, 3, 4)
plt.loglog(x,y)
plt.title("Loglog")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(which="both")
plt.subplot(2, 3, 5)
plt.semilogx(x,y)
plt.title("Semilogx")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(which="both")
plt.subplot(2, 3, 6)
plt.semilogy(x,y)
plt.title("Semilogy")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid()
plt.tight_layout()
plt.show()
#plt.savefig("image.pdf")
"""
# 3D
"""fig = plt.figure(figsize = (8,8))
ax = plt.axes(projection="3d")
ax.grid()
t = np.arange(0, 10*np.pi, np.pi/50)
x = np.sin(t)
y = np.cos(t)
ax.plot3D(x, y, t)
ax.set_title("3D Parametric Plot")
# Set axes label
ax.set_xlabel("x", labelpad=20)
ax.set_ylabel("y", labelpad=20)
ax.set_zlabel("t", labelpad=20)
plt.show()"""
#Proplem 1
"""r=3; 
phi = np.arange(0, 2*np.pi, np.pi/500, dtype=float)
x=[]; y=[]
for i in range(0,len(phi)):
  x.append(r*(phi[i] - sin(phi[i])))
  y.append(r*(1 - cos(phi[i])))
plt.figure(figsize=(10,6))
plt.plot(x,y,label="cycloid")
plt.title("Cycloid")
plt.xlabel("x",fontsize=12)
plt.ylabel("y",fontsize=12)
plt.legend(loc = 2)
plt.grid()
#plt.show()
#proplem 2
y=[]
x=np.arange(0,100,1)
for i in range(0,len(x)):
 y.append(((100*(1-0.01*x[i]**2)**2 + 0.02*x[i]**2)/((1-x[i]**2)**2 +0.1*x[i]**2))**0.5)
plt.figure(figsize=(10,10))
plt.subplot(2,2,1)  #plot
plt.plot(x,y,label="plot")
plt.title("plot")
plt.grid()
plt.subplot(2,2,2) #semilogx
plt.semilogx(x,y,label="semilogx")
plt.title("semilogx")
plt.title("plot")
plt.grid()
plt.subplot(2,2,3) #semilogy
plt.semilogx(x,y,label="semilogy")
plt.title("semilogy")
plt.title("semilogy")
plt.grid()
plt.subplot(2,2,4) #loglog
plt.semilogx(x,y,label="loglog")
plt.title("loglog")
plt.title("loglog")
plt.grid()
plt.tight_layout()
#plt.show()
#proplem 3 
y1=[]; y2=[];
for i in range(0,len(x)):
 y1.append(3+exp(-x[i])*sin(6*x[i]))
 y2.append(4+exp(-x[i])*cos(x[i]))
plt.figure(figsize=(7,7))
plt.plot(x,y1,label="y1")
plt.plot(x,y2,label="y2")
plt.grid()
plt.show()
#proplem 4
y=np.random.randn(1000)
x=np.random.randn(1000)
y=np.sort(y)
x=np.sort(x)
plt.figure(figsize=(10,10))
plt.subplot(1,2,1)
plt.bar(x,y)
plt.subplot(1,2,2)
plt.hist(x,y,histtype='bar')
plt.show()
#proplem 5
grade_dist =[42, 85, 67, 20, 5]
y=grade_dist
per=[]
for i in range(0,len(grade_dist)):
 per.append((y[i]/sum(y)*100))
plt.pie(y,labels=["A","B","C","D","F"],autopct='%i')
plt.show()
"""
#proplem 6
x=np.arange(-4,4,8/100)
y=np.arange(-3,3,6/100)
X, Y = np.meshgrid(x, y)
Z=(X*Y*(X**2-Y**2))/(X**2+Y**2)
#ax = plt.axes(projection="3d")
#plt.subplot(1,2,1,projection='3d')
#ax.plot_surface(X, Y, Z, cmap = plt.cm.cividis)
ay=plt.axes(projection="3d")
#plt.subplot(1,2,2,projection='3d')
ay.plot_wireframe(X,Y,Z)
# Set axes label
ay.set_xlabel("x", labelpad=10)
ay.set_ylabel("y", labelpad=10)
ay.set_zlabel("z", labelpad=10)

plt.show()
