# a diagonal matrix consists of only diagonal elements other are sparse

import numpy as np

a = np.array([1, 2, 1])
b = np.array([1, 1, 1])

result = a * b

print(np.diag(result))
