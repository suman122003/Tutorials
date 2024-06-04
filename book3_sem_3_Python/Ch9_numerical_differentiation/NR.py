from derivative import dfdx3

def NR(f,pr,x1,mxItr,tol):
    itr= 0
    while True:
        x2= x1 -f(pr,x1)/ dfdx3(f,pr,x1,tol)
        if abs(x2-x1) <= tol or itr> mxItr:
            break
        else:
            x1=x2
        itr += 1
    if itr < mxItr:
        return x2
    else:
        return None