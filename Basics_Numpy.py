import math
#import Basics_Numpy as np
def basic_sigmoid(x):
    """
    Compute sigmoid of x.

    Arguments:
    x -- A scalar

    Return:
    s -- sigmoid(x)
    """
    s = 1/(1+math.exp(-x))
    
    return s

print("basic_sigmoid(1) = " + str(basic_sigmoid(1)))

#t_x = np.array([1, 2, 3])
#print(np.exp(t_x)) # result is (exp(1), exp(2), exp(3))