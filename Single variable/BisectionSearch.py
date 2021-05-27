import math
import numpy as np


def get_func(variable):
    return (6*np.exp(-2*variable))+(2*np.square(variable))

def deriv_func(variable):
    return (-12*np.exp(-2*variable))+(4*variable)


def bisection_search(a,b,l):

    n = int(np.log(l/(b-a))/np.log(0.5))

    for i in range(0,n):

        lambda_k = (a+b)/2
        h = deriv_func(lambda_k)
        
        if h == 0:
            break
        elif h > 0:
            a = a
            b = lambda_k
        elif h <0:
            a = lambda_k
            b = b
        
    print("Bisection_search solution: ",(a+b)/2)

if __name__ == "__main__":
	bisection_search(-1,2,0.0001)
