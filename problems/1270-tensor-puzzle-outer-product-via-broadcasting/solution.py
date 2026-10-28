import torch

def outer(a: torch.Tensor, b: torch.Tensor) -> torch.Tensor:
    """Outer product a_i * b_j via broadcasting (no torch.outer)."""
    # Your code here
    return torch.stack([a[i]*b for i in range(a.shape[0])],axis=0)