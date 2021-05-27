import math
import numpy as np


def get_func(variable):
    return (6*np.exp(-2*variable))+(2*np.square(variable))

def deriv_func(variable):
    return (-12*np.exp(-2*variable))+(4*variable)

def double_deriv_func(variable):
    return (24*np.exp(-2*variable)) + 4


def newton_raphson(x):

    h = deriv_func(x) / double_deriv_func(x)
    if abs(h)<=0.0001:
        print("Newton_raphson method solution: ",x)
        return

    else:
        x = x - h
        newton_raphson(x)

if __name__ == "__main__":
	newton_raphson(0)
