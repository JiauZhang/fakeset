from fakeset.generator import (
    make_s_curve,
    make_swiss_roll,
)
import matplotlib.pyplot as plt

plt.style.use('_mpl-gallery')

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
points, t = make_s_curve(n_samples=2000, noise=0.2)
ax.scatter(points[:, 0], points[:, 1], points[:, 2])
plt.show()

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
points, t = make_swiss_roll(n_samples=2000, noise=0.2)
ax.scatter(points[:, 0], points[:, 1], points[:, 2])
plt.show()
