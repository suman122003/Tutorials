# 4.2 PARABOLIC PDE - FUNCTIONS

import numpy as np
import numpy.linalg as npla
import scipy.linalg as spla
import matplotlib.pyplot as plt


# FTCS Method
def parbPDE_FTCS(U0, D, hx, ht):
    '''
    Function: parbPDE_FTCS(U0, D, hx, ht)
        ARGUMENTS
    U0: list of solution at previous time step
    D: Constant in PDE
    hx, ht: Steps in x and t
        RETURNS
    U: list of solution in current time step
    '''
    lmb = D*ht/hx**2
    lmb1 = 1-2*lmb
    Nx = len(U0)
    U = [0 for i in range(Nx)]
    for i in range(1, Nx-1):
        U[i] = lmb*U0[i-1] +lmb1*U0[i] +lmb*U0[i+1]
    return U

# Solving equations in form of tridiagonal matrix
def CFtriag(aug_mat):
    '''
    Function to solve matrix equation by LU factorization (for tridiagonal matrices)
    Function: CFtriag(aug_mat)
        ARGUMENTS
    aug_mat: augmented matrix [A|b], for equation, AX = b
        RETURNS
    X: solution of the matrix equation
    '''
    ab = aug_mat
    n = len(ab)
    l = [[0 for j in range(n)] for i in range(n)]
    u = [[0 for j in range(n)] for i in range(n)]
    z = [0 for i in range(n)]
    for i in range(n-1):
        l[i][i-1] = ab[i][i-1]
        l[i][i] = ab[i][i] -l[i][i-1]*u[i-1][i]
        u[i][i+1] = ab[i][i+1]/l[i][i]
        z[i] = (ab[i][n]-l[i][i-1]*z[i-1])/l[i][i]
    l[n-1][n-2] = ab[n-1][n-2]
    l[n-1][n-1] = ab[n-1][n-1] -l[n-1][n-2]*u[n-2][n-1]
    z[n-1] = (ab[n-1][n]-l[n-1][n-2]*z[n-2])/l[n-1][n-1]
    X = [0 for i in range(n)]
    X[n-1] = z[n-1]
    for i in range(n-2, -1, -1):
        X[i] = z[i] - u[i][i+1]*X[i+1]
    return X


def parbPDE_BTCS(U0, D, hx, ht):
    '''
    Function: parbPDE_BTCS(U0, D, hx, ht)
        ARGUMENTS
    U0: list of solution at previous time step
    D: Constant in PDE
    hx, ht: Steps in x and t
        RETURNS
    U: list of solution in current time step
    '''
    lmb = D*ht/hx**2
    lmb1 = 1+2*lmb
    Nx = len(U0)
    A = [[0 for j in range(Nx+1)] for i in range(Nx)] # augmented matrix
    A[0][0], A[0][Nx] = 1, U0[0]
    A[Nx-1][Nx-1], A[Nx-1][Nx] = 1, U0[Nx-1]
    for j in range(1,Nx-1):
        A[j][j-1], A[j][j], A[j][j+1] = -lmb, lmb1, -lmb
        A[j][Nx] = U0[j]
    # U = CFtriag(A)
    Amat = np.array(A)[:,:-1]
    U = spla.inv(Amat) @ np.array(U0) # Use LU factorization
    return U
    

def parbPDE_CrNc(U0, D, hx, ht):
    '''
    Function: parbPDE_CrNc(U0, D, hx, ht)
        ARGUMENTS
    U0: list of solution at previous time step
    D: Constant in PDE
    hx, ht: Steps in x and t
        RETURNS
    U: list of solution in current time step
    '''
    lmb = D*ht/hx**2
    lmb1, lmb2 = 2+2*lmb, 2-2*lmb
    Nx = len(U0)
    A = [[0 for j in range(Nx)] for i in range(Nx)]
    A[0][0], A[Nx-1][Nx-1] = 1, 1
    B = [[0 for j in range(Nx)] for i in range(Nx)]
    B[0][0], B[Nx-1][Nx-1] = 1, 1
    for j in range(1, Nx-1):
        A[j][j-1], A[j][j], A[j][j+1] = -lmb, lmb1, -lmb
        B[j][j-1], B[j][j], B[j][j+1] = lmb, lmb2, lmb
    Aarr, Barr, U0arr = np.array(A), np.array(B), np.array(U0)
    Uarr = (spla.inv(Aarr)).dot(Barr.dot(U0arr))
    # lu, piv = spla.lu_factor(Aarr)
    # Uarr = spla.lu_solve((lu, piv), (Barr @ U0arr)) # TEST SPEED
    # barr = np.array([(Barr @ U0arr)])
    # Ab = np.concatenate((Aarr, barr.T), axis=1)
    # Uarr = CFtriag(Ab)
    return Uarr


def parbPDE_CrNc1(U0, D, hx, ht):
    '''
    Function: parbPDE_CrNc1(U0, D, hx, ht)
        ARGUMENTS
    U0: list of solution at previous time step
    D: Constant in PDE
    hx, ht: Steps in x and t
        RETURNS
    U: list of solution in current time step
    '''
    lmb = D*ht/hx**2
    lmb1, lmb2 = 2+2*lmb, 2-2*lmb
    Nx = len(U0)
    C = [[0 for j in range(Nx+1)] for i in range(Nx)]
    C[0][0], C[Nx-1][Nx-1] = 1, 1
    C[0][Nx], C[Nx-1][Nx] = U0[0], U0[Nx-1]
    for j in range(1, Nx-1):
        C[j][j-1], C[j][j], C[j][j+1] = -lmb, lmb1, -lmb
        C[j][Nx] = lmb*U0[j-1] +lmb2*U0[j] +lmb*U0[j+1]
    U = CFtriag(C)
    return U


def propTDSE_FTCS(pr, psi_Real, psi_Imaginary, V, dx, dt):
    '''
        ARGUMENTS
    pr: [hbar, m]
    psi_Real: real part of wavefunction
    psi_Imaginary: imaginary part of wavefunction
    V: Potential
    dx, dt:
        RETURNS
    psiR: real part of wavefunction
    psiI: imaginary part of wavefunction
    '''
    hbar, m = pr
    psiR, psiI = psi_Real, psi_Imaginary
    Nx =  len(psiR)
    al, be = hbar*dt/(2*m*dx**2), dt/hbar
    for i in range(1, Nx-1):
        psiR[i] = psiR[i] -al*(psiI[i-1]-2*psiI[i]+psiI[i+1]) +be*V[i]*psiI[i]
        psiI[i] = psiI[i] -al*(psiR[i-1]-2*psiR[i]+psiR[i+1]) +be*V[i]*psiR[i]
    return psiR, psiI

# Normalization
def psiNormRI(psiR, psiI, dx):
    '''
        ARGUMENTS
    psiR: list of real psi values
    psiI: list of imaginary psi values
    dx: step in x
        RETURNS
    psiR: normalized
    psiI: normalized
    '''
    Nx = len(psiR)
    psi2 = [psiR[i]**2 + psiI[i]**2 for i in range(Nx)]
    psi2arr = np.array(psi2)
    psimod2 = np.sum(psi2arr*dx)
    psiRn, psiIn = np.array(psiR)/(psimod2)**0.5, np.array(psiI)/(psimod2)**0.5
    return list(psiRn), list(psiIn)

# Solving TDSE by FTCS
def TDSE_FTCS(pr, wvpk_fn, prWv, pot_fn, prPt, x0, xN, Nx, ts, tmx, tps):
    '''
        ARGUMENTS
    pr: parameters [hbar, m]
    wvpk_fn: function for initial wave packet wvpk_fn(prWv, Nx)
    prWv: parameters for wvpk_fn
    pot_fn: function for potential pot_fn(prPt, x)
    prPt: parameters for pot_fn
    x0, xN: min and max value of x
    Nx: total no. of points in x
    ts: No. of iterations interval for real time plot
    tmx: max (final) time
    tps: Pause time plt.pause(tps)
        RETURNS
    None
    (Wave function plot)
    '''
    hbar, m = pr
    dx = (xN-x0)/(Nx-1)
    X = [x0+i*dx for i in range(Nx)]
    k0, sig = prWv[1], prWv[2]
    E = (hbar**2/(2*m))*(k0**2 + 1/(2*sig**2))
    V = pot_fn(prPt, Nx)
    Vmx = max(max(V), abs(min(V)))
    dt = hbar/(2*hbar**2/(m*dx**2) + Vmx)
    psi = [wvpk_fn(prWv, x) for x in X]     # initial
    psiR = [psi[i].real for i in range(Nx)]  # initial real part
    psiI = [psi[i].imag for i in range(Nx)]  # initial imaginary part
    psiR, psiI = psiNormRI(psiR, psiI, dx)
    psi2 = [(psiR[i]**2 +psiI[i]**2) for i in range(Nx)]
    psi23 = [3*(psiR[i]**2 +psiI[i]**2) for i in range(Nx)]
    xmn, xmx, ymx = min(X), max(X), 1.5*max(psiR)

    # Rescaling
    Efac = 0
    if Vmx != 0:
        Efac = ymx/(2*Vmx)
        Vplot = [V[i]*Efac for i in range(Nx)]
    print(f'Scaling factor={Efac}. Energy={E}, Scaled energy={E*Efac}')

    # PLOTTING
    t, iter = 0, 0    # time and iteration counting
    while t <= tmx:
        if iter % ts == 0:  # plotting at ts no. of iterations
            plt.axis([xmn, xmx, -ymx, ymx])
            if Efac != 0:
                plt.plot(X, Vplot, ':k')
                plt.axhline(E*Efac, label='E')
                plt.fill_between(X, Vplot, facecolor='grey')
            plt.plot(X, psiR, label=r'$\psi_{real}(x,t)$')
            # plt.plot(X, psiI, label=r'$\psi_{imag}(x,t)$')
            # plt.plot(X, psi2, label=r'$|\psi(x,t)|^2$')
            plt.plot(X, psi23, label=r'$3|\psi(x,t)|^2$')
            plt.text(0.8*xmx, 0.9*ymx, f't={t}')
            plt.legend(loc='lower left')
            plt.xlabel('$x$')
            plt.pause(tps)
            plt.clf()
        psiR, psiI = propTDSE_FTCS(pr, psiR, psiI, V, dx, dt)
        psi2 = [(psiR[i]**2 +psiI[i]**2) for i in range(Nx)]
        psi23 = [3*(psiR[i]**2 +psiI[i]**2) for i in range(Nx)]
        iter += 1
        t += 1
    plt.show()
    return None


def propTDSE_CrNc(pr, psiR, psiI, V, dx, dt, mxItr, tol):
    '''
        ARGUMENTS
    pr: [hbar, m]
    psiR: real part of wavefunction
    psiI: imaginary part of wavefunction
    V: Potential
    dx, dt:
    mxItr, tol:
        RETURNS
    psiR: real part of wavefunction
    psiI: imaginary part of wavefunction
    '''
    hbar, m = pr
    Nx = len(psiR)
    al, bt = hbar*dt/(4*m*dx**2), dt/(2*hbar)
    gam = [2*al + bt*V[i] for i in range(Nx)]
    psiR0 = [0 for i in range(Nx)]
    psiI0 = [0 for i in range(Nx)]
    for i in range(1, Nx-1):
        psiR0[i] = psiR[i] -al*(psiI[i-1]+psiI[i+1]) +gam[i]*psiI[i]
        psiI0[i] = psiI[i] +al*(psiR[i-1]+psiR[i+1]) -gam[i]*psiR[i]
    for itr in range(1, mxItr+1):
        err = 0
        for i in range(1, Nx-1):
            psi1 = psiR0[i] -al*(psiI[i-1]+psiI[i+1]) +gam[i]*psiI[i]
            psi2 = psiI0[i] +al*(psiR[i-1]+psiR[i+1]) -gam[i]*psiR[i]
            err1 = abs((psi1**2+psi2**2) - (psiR[i]**2+psiI[i]**2))
            if err1 > err:
                err = err1
            psiR[i], psiI[i] = psi1, psi2
        if err <= tol:
            break
    if itr < mxItr:
        return psiR, psiI
    else:
        print('function not converged! maximum iterations exceeded.')
        return None, None


def psiNormRI1(psiR, psiI, dx):    
    '''
        ARGUMENTS
    psiR: list of real psi values
    psiI: list of imaginary psi values
    dx: step in x
        RETURNS
    psiR: normalized
    psiI: normalized
    '''
    Nx = len(psiR)
    psimod2 = [psiR[i]**2 + psiI[i]**2 for i in range(Nx)]
    psiNorm1 = (psimod2[0]+psimod2[Nx-1])/2
    for i in range(1, Nx-1):
        psiNorm1 += psimod2[i]
    psiNorm1 *= dx   # normalization: power half ????
    psiR = [psiR[i]/psiNorm1**0.5 for i in range(Nx)]
    psiI = [psiI[i]/psiNorm1**0.5 for i in range(Nx)]
    return psiR, psiI

def TDSE_CrNc(pr, wvpk, prwv, pot, prpt, x0, xN, Nx, ts, tmx, tps):
    '''
        ARGUMENTS
    pr: parameters [hbar, m]
    wvpk: function for initial wave packet wvpk_fn(prWv, Nx)
    prwv: parameters for wvpk_fn
    pot: function for potential pot_fn(prPt, x)
    prpt: parameters for pot_fn
    x0, xN: min and max value of x
    Nx: total no. of points in x
    ts: No. of iterations interval for real time plot
    tmx: max (final) time
    tps: Pause time plt.pause(tps)
        RETURNS
    None
    (Wave function plot)
    '''
    hbar, m = pr
    dx = (xN-x0)/(Nx-1)
    X = [x0+i*dx for i in range(Nx)]
    sig, k0 = prwv[1], prwv[2]
    E = (hbar**2/(2*m))*(k0**2 + 1/(2*sig**2))
    V = pot(prpt, Nx)
    Vmx = max(max(V), abs(min(V)))
    dt = hbar/(hbar**2/(m*dx**2) + Vmx/2)   # wrong formula here
    psi = [wvpk(prwv, x) for x in X]     # initial
    psiR = [psi[i].real for i in range(Nx)]  # initial real part
    psiI = [psi[i].imag for i in range(Nx)]  # initial imaginary part
    psiR, psiI = psiNormRI1(psiR, psiI, dx)
    Xmn, Xmx, Ymx = min(X), max(X), 1.5*max(psiR)

    # Rescaling
    if Vmx != 0:
        Efac = Ymx/(2*Vmx)
        Vplot = [V[i]*Efac for i in range(Nx)]
    print(f'Energy of the particle = {E}, Scaled Energy = {E*Efac}')
    mxItr, tol = 100, 1e-5
    t, itr = 0, 0
    while t <= tmx:
        if itr % ts == 0:  # plotting at ts no. of iterations
            plt.axis([Xmn, Xmx, -Ymx, Ymx])
            if Efac != 0:
                plt.plot(X, Vplot, ':k')
                plt.axhline(E*Efac, label='E')
                plt.fill_between(X, Vplot, facecolor='grey')
            plt.plot(X, psiR, label=r'$\psi_{real}(x,t)$')
            psimd2 = [psiR[i]**2+psiI[i]**2 for i in range(Nx)]
            plt.plot(X, psimd2, label=r'$|\psi(x,t)|^2$')
            plt.text(0.6*Xmx, -0.9*Ymx, f't = {t}')
            plt.legend(loc='lower left')
            plt.xlabel('$x$')
            plt.pause(tps)
            plt.clf()
        psiR, psiI = propTDSE_CrNc(pr, psiR, psiI, V, dx, dt, mxItr, tol)
        itr += 1
        t += dt
    plt.show()
    return None





