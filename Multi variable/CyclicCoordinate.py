import math
import numpy as np


def get_func(c1,c2,v1,v2,lambda_k):

    return (3 - (c1+v1*lambda_k))**2 + 7*((c2+v2*lambda_k) - (c1+v1*lambda_k)**2)**2


# Golden section method of optimization

phi = (1 + math.sqrt(5))/2
resphi = 2 - phi

def golden_section_search(a, c, b, eps,c1,c2,v1,v2):

    if abs(a - b) < eps:
        return (a+b)/2
    
    d = c + resphi*(b - c)
    func_d, func_c = get_func(c1,c2,v1,v2,d), get_func(c1,c2,v1,v2,c)
    if func_d < func_c:
        return golden_section_search(c,d,b,eps,c1,c2,v1,v2)
    else:
        return golden_section_search(d,c,a,eps,c1,c2,v1,v2)


# Cyclic Coordinate method of optimization

def  cyclic_coordinate_method(x,y,d_i,j,eps,count):
    count +=1
    x_prev = x
    for i in range(0,j):
        lambda_j = golden_section_search(-5,0,5,eps,y[0],y[1],d_i[i][0],d_i[i][1])
        y = np.add(y, np.multiply(lambda_j,d_i[i]))

    x = y
    if abs(np.sum(np.subtract(x_prev,x)))<eps:
        print("Cyclic coordinate method Solution: ", x, count)
        return
    else:
        cyclic_coordinate_method(x,y,d_i,2,eps,count)


if __name__ == "__main__":
	x = [0,0]
	d_i = [[1,0],[0,1]]
	y = x

	cyclic_coordinate_method(x,y,d_i,2,0.0007,count=1)
