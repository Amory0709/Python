'''
To create a matrix look like this:
 1 1 0 0 0 0 0 
 1 1 1 0 0 0 0 
 0 1 1 1 0 0 0 
 0 0 1 1 1 0 0 
 0 0 0 1 1 1 0 
 0 0 0 0 1 1 1 
 0 0 0 0 0 1 1 
 
'''

import numpy as np

# generate matrix
a = np.zeros((7,7),int)

# change diag, fill_diagnoal generate inplace
np.fill_diagonal(a, 1)
np.fill_diagonal(a[1:], 1)
np.fill_diagonal(a[:,1:], 1)
