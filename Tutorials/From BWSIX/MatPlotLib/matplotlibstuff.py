import matplotlib as mpl
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

plt.style.use('seaborn-v0_8-whitegrid')

# step 1
fig = plt.figure(figsize = (10,5))
ax1 = fig.add_subplot(2,2,1)
ax2 = fig.add_subplot(2,2,3)
ax3 = fig.add_subplot(1,2,2)

# step2
x_values = np.linspace(-5,5,200)

# step 3
ax1.set_title("Linear")
ax1.set_xlabel("x")
ax1.set_ylabel("y")
ax1.plot(x_values, x_values, linestyle='dashed', color = 'blue', marker="o", label='Linear')

# step 4
f = lambda x: x**2
ax2.set_title("Quadratic")
ax2.set_xlabel("x")
ax2.set_ylabel("$x^2$")
ax2.set(xlim=(-5,5), ylim=(0,25))
ax2.plot(x_values, f(x_values), linestyle='solid', color='red', marker="*", label='Quadratic')

# step 5
ax3.set_title("Sine, Cosine, Sine + Cosine")
ax3.set_xlabel("x")
ax3.set_ylabel("y")
ax3.plot(x_values, np.sin(x_values), linestyle='solid', color='red', label='Sine')
ax3.plot(x_values, np.cos(x_values), linestyle='dashed', color='green', label='Cosine')
ax3.plot(x_values, (np.sin(x_values) + np.cos(x_values)), linestyle='dotted', color='blue', label = 'Sine + Cosine')
ax3.legend(loc='upper left', bbox_to_anchor=(1,1)) # 'upper left' means that corner of the legend attaches to bbox_to_anchor (1,1) coordinate

# step 6

# step 7
fig.tight_layout()

plt.show()