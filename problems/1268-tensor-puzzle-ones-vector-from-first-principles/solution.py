import torch

def ones(n: int) -> torch.Tensor:
    """Return a length-n float vector of ones without calling torch.ones."""
    # Your code here
    return torch.tensor([1]).to(torch.float32).repeat(n)
