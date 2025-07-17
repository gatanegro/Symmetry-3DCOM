import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# --- Collatz step ---


def collatz_step(n):
    return n // 2 if n % 2 == 0 else 3 * n + 1

# --- Recursive orbit mod 9 ---


def recursive_orbit(n0, depth=15):
    orbit = []
    n = n0
    for _ in range(depth):
        n = collatz_step(n)
        orbit.append(n % 9 if n % 9 != 0 else 9)  # Replace 0 with 9
    return orbit

# --- Spiral coordinates for recursive orbit ---


def circle_coordinates(orbit):
    coords = []
    for i, val in enumerate(orbit):
        angle = (val - 1) * 2 * np.pi / 9  # Mod 9 symmetry angles
        radius = 1 + i * 0.2               # Spiral out per recursion step
        x = radius * np.cos(angle)
        y = radius * np.sin(angle)
        coords.append((x, y))
    return coords


# --- Initial parameters ---
start_n = 19
depth = 20

# --- Create plot ---
fig, ax = plt.subplots(figsize=(8, 8))
plt.subplots_adjust(left=0.2, bottom=0.3)
ax.set_title("3DCOM Recursive Orbit Spiral (Mod-9 Symmetry)")
ax.axis('equal')
ax.axis('off')

# --- Initial data ---
orbit_vals = recursive_orbit(start_n, depth)
coords = circle_coordinates(orbit_vals)
xs, ys = zip(*coords)
points, = ax.plot(xs, ys, '-o', color='blue', markersize=5)

# --- Sliders ---
ax_n = plt.axes([0.25, 0.15, 0.65, 0.03])
slider_n = Slider(ax_n, 'Start n', 1, 100, valinit=start_n, valstep=1)

ax_depth = plt.axes([0.25, 0.10, 0.65, 0.03])
slider_depth = Slider(ax_depth, 'Depth', 5, 50, valinit=depth, valstep=1)

# --- Update function ---


def update(val):
    n = int(slider_n.val)
    d = int(slider_depth.val)
    new_orbit = recursive_orbit(n, d)
    new_coords = circle_coordinates(new_orbit)
    xs, ys = zip(*new_coords)
    points.set_data(xs, ys)
    fig.canvas.draw_idle()


slider_n.on_changed(update)
slider_depth.on_changed(update)

plt.show()
