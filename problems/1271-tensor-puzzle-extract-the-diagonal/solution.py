import numpy as np

def diag(A: np.ndarray) -> np.ndarray:
    """Return the main diagonal of square matrix A."""
    # Your code here
    t_flat = A.flatten()
    return t_flat[::A.shape[0]+1]