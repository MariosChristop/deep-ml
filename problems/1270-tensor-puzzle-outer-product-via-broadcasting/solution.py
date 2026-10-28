import numpy as np

def outer(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    """Outer product of 1-D arrays a and b via broadcasting."""
    # Your code here
    return np.stack([a[i]*b for i in range(a.shape[0])],axis=0)
