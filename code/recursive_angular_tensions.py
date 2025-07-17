import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# --- Constants ---
alpha = 1.035  # Bridge Formula scaling
L0 = 1.0       # Base radius unit

# --- Recursive Functions ---


def R_n(n):
    return alpha ** (-n) * L0


def compute_S(n, delta_theta):
    R = R_n(n)
    return R**2 * delta_theta**2


# --- Plot Setup ---
fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.35)

theta_vals = np.linspace(0, 2 * np.pi, 500)
n0 = 5
S_vals = [compute_S(n0, dtheta) for dtheta in theta_vals]

line, = ax.plot(theta_vals, S_vals, label='S(n, Δθ)', color='blue')
ax.set_title("Recursive Angular Field Tension $S(n, \Delta\\theta)$")
ax.set_xlabel("Δθ (radians)")
ax.set_ylabel("Tension $S$")
ax.legend()
ax.grid(True)

# --- Slider ---
ax_n = plt.axes([0.25, 0.20, 0.65, 0.03])
slider_n = Slider(ax_n, 'n (layer)', 1, 30, valinit=n0, valstep=1)


def update(val):
    n = int(slider_n.val)
    S_vals = [compute_S(n, dtheta) for dtheta in theta_vals]
    line.set_ydata(S_vals)
    fig.canvas.draw_idle()


slider_n.on_changed(update)

plt.show()
