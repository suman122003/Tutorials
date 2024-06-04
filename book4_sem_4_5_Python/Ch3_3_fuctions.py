#       CHAPTER 3: BOUNDARY VALUE PROBLEMS - USEFUL FUNCTIONS

import numpy as np


# Normalization
def psiNorm(psi, dx):
    N = len(psi)
    psi2 = [psi[i]**2 for i in range(N)]
    psi2arr = np.array(psi2)
    psimod2 = np.sum(psi2arr*dx)
    norm_psi = np.array(psi)/(psimod2)**0.5
    return norm_psi

# Propagator with central difference calculation
def prop_central_diff(pr, p, q, r, x, y, dx):
    '''
    y'' + py' + qy + r = 0
    p = p(x), q = q(lb, x), r = r(x)
    '''
    N = len(x)
    yy = [y[i] for i in range(N)]
    for i in range(2, N):
        a = 2 + dx**2 *q(pr, x[i-1])
        b = -(1 + dx/2 *p(x[i-1]))
        c = dx**2 *r(x[i-1])
        d = 1 - dx/2 *p(x[i-1])
        yy[i] = a/d *yy[i-1] + b/d *yy[i-2] + c/d
    return yy

# Determination of eigenvalue and eigenfunction
def center_diff_eigval(pr_min, pr_max, p, q, r, x0, y0, xN, yN, y1, dx, nodes, tol, max_itr):
    '''
    x0, y0 - left boundary condition
    xN, yN - right boundary condition
    y1 - estimation of solution at the next point after left boundary (y0)
    '''
    N = int((xN -x0)/dx)
    dx = (xN -x0)/N
    x = [x0 +i*dx for i in range(N+1)]
    y = [0 for i in range(N+1)]
    y[0], y[1], y[N] = y0, y1, yN
    itr = 0
    while abs(pr_max - pr_min) >  tol and itr < max_itr:
        pr = 0.5 *(pr_min + pr_max)  # bisection method
        yy = prop_central_diff(pr, p, q, r, x, y, dx)
        cnt = 0  # count
        for i in range(1, N-2):
            if yy[i]*yy[i+1] < 0:
                cnt += 1
        if cnt > nodes:
            pr_max = pr
        elif cnt < nodes:
            pr_min = pr
        else:
            if yy[N-1] > yN:
                pr_min = pr
            elif yy[N-1] < yN:
                pr_max = pr
            itr += 1
    if itr < max_itr:
        return pr, x, yy
    else:
        return None, None, None
    
# Propagator with Numerov Method
def propNumerov(pr, q, r, x, y, dx):
    '''
    q = q(lambda, x), r = r(x)
    x - x array of propagation
    y - y array of propagation (a zero list generally)
    dx - increment along x axis
    yy - returned y array
    '''
    N = len(x)
    yy = [y[i] for i in range(N)]
    for i in range(2, N):
        a = 2*(1 + 5*dx**2/12 * q(pr, x[i-1]))
        b = -(1 - dx**2/12 * q(pr, x[i-2]))
        c = dx**2/12 * (r(x[0]) + 10*r(x[i-1]) + r(x[i-2]))
        d = 1 - dx**2/12 * q(pr, x[i])
        yy[i] = a/d * yy[i-1] + b/d * yy[i-2] + c/d
    return yy

# Solving the eigenvalue problem
def NumerovEigVal(prMin, prMax, q, r, x0, y0, xN, yN, y1, dx, nodes, tol, mxItr):
    '''
    prMin, prMax - lower and upper limit of eigenvalue
    q = q(lambda, x), r = r(x)
    x0, y0 - left boundary conditions
    xN, yN - right boundary conditions
    y1 - next y value after y0
    dx - increment along x axis
    nodes - no. of nodes of eigenvalue
    tol - tolerance
    mxItr - maximum allowed iteration
    Return: pr, x, yy
        pr - eigenvalue
        x - x array of solution
        yy = y array of solution
    '''
    N = int((xN-x0)/dx)
    dx = (xN - x0)/N
    x = [x0 + i*dx for i in range(N+1)]
    y = [0 for i in range(N+1)]  # zero list
    y[0], y[1], y[N] = y0, y1, yN
    itr = 0
    # tol = 1e-6  # tolerance

    while abs(prMax-prMin) > tol and itr < mxItr:
        pr = 0.5*(prMin + prMax) # proceeding to bisection method
        yy = propNumerov(pr, q, r, x, y, dx)
        cnt = 0
        for i in range(1, N-2):
            if yy[i]*yy[i+1]<0:
                cnt += 1
        if cnt > nodes:
            prMax = pr
        elif cnt < nodes:
            prMin = pr
        else:
            if yy[N-1] > yN:
                prMin = pr
            elif yy[N-1] < yN:
                prMax = pr
        itr += 1
    if itr < mxItr:
        return pr, x, yy
    else:
        return None, None, None