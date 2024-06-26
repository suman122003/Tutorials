# 4.1 ELLIPTICAL PDE - FUNCTIONS

import numpy as np

# By Central Difference Method
def elpPDE_CD(f,g, Xmn,Xmx,Ymn,Ymx, hx,hy):
    '''
    Function: elpPDE_CD(f, g, Xmn, Xmx, Ymn, Ymx, hx, hy)
        ARGUMENTS
    f: function at RHS of Poisson's equation
    g: function for boundary conditions
    Xmn, Xmx: min and max value of x
    Ymn, Ymx: min and max value of y
    hx, hy: Steps in x and y
        RETURNS
    x: 1D array containing x values
    y: 1D array containing y values
    u: 2D array containing solution
    '''
    mxitr, tol = int(1e6), 1e-4
    bnd = [Xmn,Xmx,Ymn,Ymx]
    Nx = int((Xmx-Xmn)/hx)
    hx = (Xmx-Xmn)/Nx
    x = [Xmn + i*hx for i in range(Nx+1)]
    Ny = int((Ymx-Ymn)/hy)
    hy = (Ymx-Ymn)/Ny
    y = [Ymn + j*hy for j in range(Nx+1)]

    U = [[0 for j in range(Ny+1)] for i in range(Nx+1)]  # 0 2D array
    for i in range(Nx+1):
        U[i][0] = g(bnd, x[i], y[0])
        U[i][Ny] = g(bnd, x[i], y[Ny])
    for j in range(Ny+1):
        U[0][j] = g(bnd, x[0], y[j])
        U[Nx][j] = g(bnd, x[Nx], y[j])
    fij = [[f(x[i],y[j]) for j in range(Ny)] for i in range(Nx)]
    lmb = (hx/hy)**2
    lmb1 = 2*(1+lmb)

    for itr in range(1, mxitr+1):   # Gauss-Seidel iteration loop
        err = 0
        for j in range(1,Ny):
            for i in range(1,Nx):
                uij = (1/lmb1)*(U[i-1][j]+U[i+1][j] + lmb*(U[i][j-1]+U[i][j+1])- (hx**2)*fij[i][j])
                if uij != 0:
                    eij = 1 - U[i][j]/uij # relative error
                else:
                    eij = uij - U[i][j]   # absolute error
                err = max(err, abs(eij))
                U[i][j] = uij
                if err <= tol:
                    break
        if itr >= mxitr:
            print('max. no. of iterations exceeded!')
        else:
            # print('no. of iterations', itr)
            return x, y, U
                
