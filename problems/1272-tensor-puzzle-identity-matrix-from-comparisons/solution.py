import numpy as np

def eye(n: int) -> np.ndarray:
    """n x n identity matrix without np.eye."""
    # Your code here
    t=np.expand_dims(np.arange(n),axis=1)
    t_T = np.transpose(t)
    return np.float64(np.equal(t, t_T))