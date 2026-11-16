import torch

def eye(n: int) -> torch.Tensor:
    """n x n identity via comparisons (no torch.eye)."""
    # Your code here
    t = torch.arange(n).unsqueeze(-1)
    t_T = torch.transpose(t,0,-1)
    return torch.eq(t,t_T).to(torch.float64)
