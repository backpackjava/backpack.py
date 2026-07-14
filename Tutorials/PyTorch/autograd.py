import torch
import matplotlib.pyplot as mpl
import math
a = torch.linspace(0., 2. * math.pi, steps=25, requires_grad=True)
print(a)

b = torch.sin(a)
# mpl.plot(a.detach(), b.detach())
# mpl.show()

c = 2 * b
d = c + 1
print(d.grad_fn)
print(d.grad_fn.next_functions[0][0]) 
out = d.sum()

out.backward()
print(a.grad)
mpl.plot(a.detach(), a.grad.detach())
mpl.plot(a.detach(), b.detach())
mpl.show()