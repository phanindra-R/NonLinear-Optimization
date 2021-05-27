import math
import numpy as np


def get_func(variable):
    return (6*np.exp(-2*variable))+(2*np.square(variable))

def deriv_func(variable):
    return (-12*np.exp(-2*variable))+(4*variable)


def fibonacci_generator(n):
    if n < 1:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_generator(n - 1) + fibonacci_generator(n - 2)


def fibonacci_search(a,b,l,eps,lambda_k,mu_k,n,k):

    if k == 1:
        lambda_k = a + (fibonacci_generator(n-2)/fibonacci_generator(n))*(b-a)
        mu_k = a + (fibonacci_generator(n-1)/fibonacci_generator(n))*(b-a)

    f_lambda_k = get_func(lambda_k)
    f_mu_k = get_func(mu_k)

    if f_lambda_k > f_mu_k:
        a = lambda_k
        lambda_k = mu_k
        mu_k = a + (fibonacci_generator(n-k-1)/fibonacci_generator(n-k))*(b-a)

    else:
        b = mu_k
        mu_k = lambda_k
        lambda_k = a + (fibonacci_generator(n-k-2)/fibonacci_generator(n-k))*(b-a)

    if k == n-2:
        mu_k = lambda_k + eps
        if get_func(lambda_k)>get_func(mu_k):
            print("fibonacci_search Solution: ",(lambda_k+b)/2)
        else:
            print("fibonacci_search Solution: ",(a+mu_k)/2)
        return
    else:
        k += 1
        fibonacci_search(a,b,l,eps,lambda_k,mu_k,n,k)


if __name__ == "__main__":
	fibonacci_search(2,-1,0.001,0.001,1,1,27,1)
