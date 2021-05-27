import math
import numpy as np

def get_func(variable):
    return (6*np.exp(-2*variable))+(2*np.square(variable))

def Dichotomous_search(a,b,l,epsilon):
    
    if np.absolute(b - a) < l:
        print("Dichotomous_search solution: ", (a+b)/2)
        return 

    else:
        lambda_k = ((a+b)/2) - epsilon
        mu_k = ((a+b)/2) + epsilon

        if get_func(lambda_k) < get_func(mu_k):

            Dichotomous_search(a,mu_k,l,epsilon)

        else:
            Dichotomous_search(lambda_k,b,l,epsilon)

if __name__ == "__main__":
	Dichotomous_search(-1,2,0.0001,0.00001)
