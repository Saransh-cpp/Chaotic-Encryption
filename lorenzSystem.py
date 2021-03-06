import numpy as np
import matplotlib.pyplot as plt

def lorenz_key(xinit, yinit, zinit, num_steps):
    dt = 0.01

    xs = np.empty(num_steps + 1)
    ys = np.empty(num_steps + 1)
    zs = np.empty(num_steps + 1)

    # Initial values
    xs[0], ys[0], zs[0] = (xinit, yinit, zinit)

    s = 10
    r = 28
    b = 2.667

    # System of equations
    for i in range(num_steps):
        xs[i + 1] = xs[i] + (s * (ys[i] - xs[i]) * dt)
        ys[i + 1] = ys[i] + ((xs[i] * (r - zs[i]) - ys[i]) * dt)
        zs[i + 1] = zs[i] + ((xs[i] * ys[i] - b * zs[i]) * dt)

    # fig = plt.figure()
    # ax = fig.gca(projection='3d')

    # ax.plot(xs, ys, zs)
    # plt.show()

    return xs, ys, zs
# Plotting
# fig = plt.figure()
# ax = fig.gca(projection='3d')

# ax.plot(xs, ys, zs)
# plt.show()

# lorenz_key(0.01, 0.02, 0.03, 1000)
