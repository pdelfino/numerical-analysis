from pylab import *
import matplotlib

def n(j,xc,x):
    n = 1
    for i in arange(j):
        n *= (xc-x[i])

    return n
def a(j,l,x,y):
    if j==0:
        return y[0]
    elif j-l==1 :
        return (y[j]-y[l])/(x[j]-x[l])
    else:
        return (a(j,l+1,x,y)-a(j-1,l,x,y))/(x[j]-x[l])
        

def N(xc,x,y):
    N = 0
    for j in range(len(x)):
        N += a(j,0,x,y)*n(j,xc,x)
    
    return N

x = [0,1,2]
y = [-1,1,5]

#for testing
xc = 3

yc = N(xc,x,y)
"""
print ''
print xc, yc
#plot
print ("u", u)
u = N(t,x,y)
plot(t,u)
grid(True)
show()
"""
t = linspace(-7,7,100)

u = N(t,x,y)
I = np.arange(0,5,0.1)
plt.plot(I, u)
plt.plot(x,y,"ro")
plt.show()
