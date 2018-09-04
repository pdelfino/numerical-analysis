import numpy as np
import matplotlib.pyplot as plt

def Polynomial(t,X,Y):

    A=Y
    B=Y
    n=len(A)
    C = []

    for j in range(1,n):

        A=list(B)
        C.append([j-1])
        for i in range(j,n):
            B[i] = (A[i]-A[i-1])/(X[i]-X[i-j])
    C.append(B[n-1])
    P=1
    S = []
    for k in range(n):
        S = S+(P*(C[k])) 
        P= P*(t-X[k])
    return S

X = [2,0,5,3]

Y = [1,-1,10,-4]

I = np.arange(0,5,0.1)

print (I)

plt.plot(X,Y,"ro")
plt.plot(I, Polynomial(I,X,Y), "b")
plt.show()


