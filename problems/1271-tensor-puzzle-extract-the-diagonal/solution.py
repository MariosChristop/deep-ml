import torch

def diag(A: torch.Tensor) -> torch.Tensor:
    """Extract the main diagonal of square A without torch.diag."""
    # Your code here
    return A.flatten()[::A.shape[0]+1]
