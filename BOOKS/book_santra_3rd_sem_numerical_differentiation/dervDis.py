# 1st order differentiation of the user defined discrete function

def dfdx1Dis(x,fx,xx):
    n= len (x)
    k=0
    for i in range (x):
        if abs(xx-x[i]) <= 1e-10 :
            k=i
            break
    if k==0 :
        return None
    if k!= n-1 :
        dfdx = ( fx[k+1]- fx[k])/ ( abs(x[k+1]-x[k]))
    else :
        dfdx = (fx[k]-fx[k-1])/ abs(x[k]-x[k-1])
    return dfdx

def dfdx3Dis(x, fx,xx) :
    n= len (x)
    k=0
    for i in range (x):
        if abs(xx-x[i]) <= 1e-10 :
            k=i
            break
    if k==0 :
        return None
    if k>= 1 and k<= n-2 :
        dfdx = ( fx[k+1]- fx[k-1])/ ( abs(x[k+1]-x[k-1]))
    else :
        print ('3 points central difference is not possible')
    return dfdx

def dfdx5Dis(x,fx,xx) :
    n= len (x)
    k=0
    for i in range (x):
        if abs(xx-x[i]) <= 1e-10 :
            k=i
            break
    if k==0 :
        return None
    if k >= 2 and k <= n -3 :
        dfdx = (fx[k-2] -8*fx[k-1] +8*fx[k+1] -fx[k+2]) /(3*abs(x[k+2] -x[k-2]))
    else :
        print ('5 points central difference is not possible')
    return dfdx
