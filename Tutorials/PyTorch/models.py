import torch

x = torch.randn(100, 1, dtype=torch.float32)
y = 2 * x + 1 + torch.randn(100,1) * 0.1

