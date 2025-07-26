

import numpy as np
import time
#import scipy   Enable for specific functions

# Start timing
start = time.perf_counter()#Timer beginning

# Gauss–Legendre 7-point Roots and Weights
L_weights = np.array([
    0.1294849661688697, 0.2797053914892766, 0.3818300505051189,
    0.4179591836734694, 0.3818300505051189, 0.2797053914892766,
    0.1294849661688697])
L_roots = np.array([
    -0.9491079123427585, -0.7415311855993945, -0.4058451513773972,
     0.0, 0.4058451513773972, 0.7415311855993945,
     0.9491079123427585])

# Kronrod 15-point Roots and Weights
K_weights = np.array([
    0.0229353220105292, 0.0630920926299785, 0.1047900103222502,
    0.1406532597155259, 0.1690047266392679, 0.1903505780647854,
    0.2044329400752989, 0.2094821410847278, 0.2044329400752989,
    0.1903505780647854, 0.1690047266392679, 0.1406532597155259,
    0.1047900103222502, 0.0630920926299785, 0.0229353220105292
])
K_roots = np.array([
    -0.9914553711208126, -0.9491079123427585, -0.8648644233597691,
    -0.7415311855993945, -0.5860872354676911, -0.4058451513773972,
    -0.2077849550078985,  0.0000000000000000,  0.2077849550078985,
     0.4058451513773972,  0.5860872354676911,  0.7415311855993945,
     0.8648644233597691,  0.9491079123427585,  0.9914553711208126
])

# Integration limits
Lower = np.array([1,1,2]) #Lower Limit
Upper = np.array([10,10,5]) #Upper Limit

# Multidimensional Function to Integrate
def f(x): # Write the functions in terms of x[0] .. x[n]
    #"""Sample function for integration."""
    return  x[0]**2 + np.log(x[2]**2) - np.sin(x[2]**2)

# General n-dimensional quadrature
def QUAD(weights, roots):
    n = len(Lower)  #Length of lower limit array to recognize the number of variables
    m = len(weights) #Length of the respective weight array to know the number of points to evalaute
    mid = 0.5 * (Lower + Upper) #Midpoint
    half = 0.5 * (Upper - Lower) #Halfwidth

    result = 0.0
    index = [0] * n #Index array with n number of zeroes for odometer logic
    x = np.zeros(n) # setting a vector x that has n zeroes which will be filled later

    while True:
        w = 1.0 #initializing weight which will be multiplied by later evaluated weights
        for i in range(n):
            x[i] = mid[i] + half[i] * roots[index[i]]#Evaluating the terms inside the function to be evalauated
            w *= weights[index[i]] #product of weights 
        result += w * f(x)  # weight times funcion, crux of quadrature

        # Increment odometer
        for i in range(n - 1, -1, -1): # odometer logic that makes index go [0,0], [0,1] etc depending on the number of variables
            index[i] += 1 # increments odometer by one
            if index[i] < m: #while i goes up until the dimension of variables, m makes all permutation of products of weights and fucntion possible
                break
            index[i] = 0
        else:
            break

    return result * np.prod(half) #final integral

# Evaluating the function
I_GL = QUAD(L_weights, L_roots)
I_GK = QUAD(K_weights, K_roots)


Avg_val = 0.5*(I_GL + I_GK)
GL_Dev = np.abs(I_GL - Avg_val)
GK_Dev = np.abs(I_GK - Avg_val)
Avg_dev = 0.5*(GL_Dev + GK_Dev)
Precision = (Avg_dev/Avg_val)*100 #Precision Percentage
end   = time.perf_counter()
print("Gauss-Legendre:", I_GL) #Gauss-Legendre Output
print("Gauss-Kronrod :", I_GK) #Gauss-Kronrod Output
print("Precision:", Precision ) #Precision Output
print(f"Elapsed time: {end-start:.8f} s") #Timer Output

