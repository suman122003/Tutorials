# demonstration of tangent and normals
import matplotlib.pyplot as plt
from derivative import dfdx3

def f(pr,x):
    return x**2

tol= 1e-6
x0= 0.5
m= dfdx3(f, None, x0, tol)
