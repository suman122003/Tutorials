# 4.1 ELLIPTICAL PDE - FUNCTIONS

import numpy as np

# By Central Difference Method
def elpPDE_CD(f,g, Xmn,Xmx,Ymn,Ymx, hx,hy):
    '''
Function: elpPDE_CD(f, g, Xmn, Xmx, Ymn, Ymx, hx, hy)
Arguments:
    f: function at RHS of Poisson's equation
    g: function for boundary conditions
    Xmn, Xmx:
    Ymn, Ymx:
    hx, hy:
Returns:
    x: 1D array containing x values
    y: 1D array containing y values
    u: 2D array containing solution
    '''
    mxitr, tol = 1e6, 1e-4
    bnd = [Xmn,Xmx,Ymn,Ymx]
    Nx = int((Xmx-Xmn)/hx)
    hx = (Xmx-Xmn)/Nx
    x = [Xmn + i*hx for i in range(Nx+1)]
    Ny = int((Ymx-Ymn)/hy)
    hy = (Ymx-Ymn)/Ny
    y = [Ymn + j*hy for j in range(Nx+1)]

    u = [[0 for j in range(Ny+1)] for i in range(Nx+1)]  # 0 2D array
    for i in range(Nx+1):
        u[i][0] = g(bnd, x[i], y[0])
        u[i][Ny] = g(bnd, x[i], y[Ny])
    for j in range(Ny+1):
        u[0][j] = g(bnd, x[0], y[j])
        u[Nx][j] = g(bnd, x[Nx], y[j])
    fij = [[f(x[i],y[j]) for j in range(Ny)] for i in range(Nx)]
    lmb = (hx/hy)**2
    lmb1 = 2*(1+lmb)

    for itr in range(1, mxitr+1):   # Gauss-Seidel iteration loop
        err = 0
        for j in range(1,Ny):
            for i in range(1,Nx):
                uij = (1/lmb1)*(u[i-1][j]+u[i+1][j] + lmb*(u[i][j-1]+u[i][j+1])- hx**2*fij)
                if uij != 0:
                    eij = 1 - u[i][j]/uij # relative error
                else:
                    eij = uij - u[i][j]   # absolute error
                err = max(err, abs(eij))
                u[i][j] = uij
                if err <= tol:
                    break
        if itr >= mxitr:
            print('max. no. of iterations exceeded!')
        else:
            print('no. of iterations', itr)
            return x, y, u
                
