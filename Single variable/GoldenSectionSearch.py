import math
import numpy as np

def get_func(variable):
    return (6*np.exp(-2*variable))+(2*np.square(variable))


alpha = 0.618

def golden_section_search(a, b, alpha, abs, lambda_k, mu_k, k):

    if np.absolute(a - b) < abs:
        print("golden_section_search solution: ",(a + b)/2)
        print(f"In {k} Iterations.")
        return
    
    if get_func(lambda_k) > get_func(mu_k):
        a = lambda_k
        lambda_k = mu_k
        mu_k = a + (alpha)*(b-a)
        golden_section_search(a, b, alpha, abs, lambda_k, mu_k, k+1)
    else:
        b  = mu_k
        mu_k = lambda_k
        lambda_k = a + (1-alpha)*(b-a)
        golden_section_search(a, b, alpha, abs, lambda_k, mu_k, k+1)

if __name__ == "__main__":
	a,b = -1,2
	lambda_k = a + (1-alpha)*(b-a)
	mu_k = a + (alpha)*(b-a)
	golden_section_search(a, b, alpha,0.0001,lambda_k,mu_k,1)
