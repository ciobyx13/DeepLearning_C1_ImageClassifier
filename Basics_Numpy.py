import math
import numpy as np
def basic_sigmoid(x):
    s=1/(1+math.exp(-x))
    return s

def sigmoid(x):
    s=1/(1+np.exp(-x))
    return s

def sigmoid_derivative(x):
    s=sigmoid(x)
    ds = s*(1-s)
    return ds

def image2vector(image):
    v= image.reshape(image.shape[0]*image.shape[1]*image.shape[2],1)
    return v

print("basic_sigmoid(1) = " + str(basic_sigmoid(1)))

t_x = np.array([1, 2, 3])
print(np.exp(t_x)) # result is (exp(1), exp(2), exp(3))
print (t_x + 3)
print("sigmoid(t_x) = " + str(sigmoid(t_x)))
print ("sigmoid_derivative(t_x) = " + str(sigmoid_derivative(t_x)))
t_image = np.array([[[ 0.67826139,  0.29380381],
                     [ 0.90714982,  0.52835647],
                     [ 0.4215251 ,  0.45017551]],

                   [[ 0.92814219,  0.96677647],
                    [ 0.85304703,  0.52351845],
                    [ 0.19981397,  0.27417313]],

                   [[ 0.60659855,  0.00533165],
                    [ 0.10820313,  0.49978937],
                    [ 0.34144279,  0.94630077]]])

print ("image2vector(image) = " + str(image2vector(t_image)))