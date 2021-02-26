import numpy as np
import matplotlib.pyplot as plt

dt = 0.01
num_steps = 10000

xs = np.empty(num_steps + 1)
ys = np.empty(num_steps + 1)
zs = np.empty(num_steps + 1)

# Initial values
xs[0], ys[0], zs[0] = (0.1, 1, 1.05)

s = 10
r = 28
b = 2.667

# System of equations
for i in range(num_steps):
    xs[i + 1] = xs[i] + (s * (ys[i] - xs[i]) * dt)
    ys[i + 1] = ys[i] + ((xs[i] - (r - zs[i]) - ys[i]) * dt)
    zs[i + 1] = zs[i] + ((xs[i] * ys[i] - b * zs[i]) * dt)

print(xs, ys, zs)
# Plotting
fig = plt.figure()
ax = fig.gca(projection='3d')

ax.plot(xs, ys, zs)
plt.show()
