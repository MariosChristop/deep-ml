import numpy as np

def eye(n: int) -> np.ndarray:
    """n x n identity matrix without np.eye."""
    # Your code here
    test = np.zeros((n,n), dtype=np.float64)
    for i in np.arange(n):
        for j in np.arange(n):
            if i==j:
                test[i,j]=1.0
    if n==1:
        return [[1.]]
    return np.float64(test)