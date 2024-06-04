# 1st order differentiation
def dfdx1(f,pr,x,tol):
    # one point forward difference method
    h=0.1
    dfdx10= (f(pr,x+h)-f(pr,x))/h
    while True:
        h*=0.5
        dfdx2= (f(pr,x+h)-f(pr,x))/h
        if abs(dfdx2-dfdx10)<=tol:
            break
        else:
            dfdx10=dfdx2
    return dfdx2

def dfdx3(f,pr,x,tol):
    # 3 points central difference method
    h=0.1
    dfdx1=(f(pr,x+h)-f(pr,x-h))/(2*h)
    while True:
        h*=0.5
        dfdx2= (f(pr,x+h)-f(pr,x-h))/(2*h)
        if abs(dfdx2-dfdx1) <= tol :
            break
        else :
            dfdx1=dfdx2
    return dfdx2

def dfdx5(f,pr,x,tol) :
    # 5 points central difference method
    h=0.1
    dfdx1 = (f(pr,x-2*h) - 8*f(pr,x-h)+ 8*f(pr,x+h) - f(pr,x+2*h))/(12*h)
    while True:
        h*= 0.5
        dfdx2 = (f(pr,x-2*h) - 8*f(pr,x-h)+ 8*f(pr,x+h) - f(pr,x+2*h))/(12*h)
        if abs(dfdx2-dfdx1) <= tol :
            break
        else :
            dfdx1 = dfdx2
    return dfdx2
