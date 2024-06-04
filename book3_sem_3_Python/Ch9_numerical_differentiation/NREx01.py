# determine roots of the equation x**2 -3x +2.

from NR import NR
def f(pr,x):
    return x**2 -3*x +2
mxItr= 1000
x1= float(input('enter the initial guess: '))
x= NR(f, None, x1, mxItr, 1e-6)
if x!= None:
    print('solution is x= %9.5f'% (x))
    print('verification f(%9.5f)= %9.5f'% (x, f(None, x)))
else:
    print('no solution found. maximum iteration reached')
