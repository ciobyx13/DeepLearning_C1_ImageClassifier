#+begin_src python
import numpy as np

x = np.random.randn(4,3)

y = np.sum(x, axis = 1, keepdims = True) 

print (y.shape)
#+end_src