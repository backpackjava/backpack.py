import torch

x = torch.arange(12, dtype=torch.float32)

x.resize_(3,4)

x.squeeze_(1)

print(x)