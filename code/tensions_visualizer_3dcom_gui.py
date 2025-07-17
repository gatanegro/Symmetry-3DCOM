import tkinter as tk
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# === Constants (Full Precision) ===
alpha = 0.007297352564305367
LZ = 1.2349822806740639
pi = np.pi

# === Tensor Angular Function (with Deformation) ===


def angular_tensor(n, theta):
    # Exponential tensor decay with nonlinear stretch
    Rn = alpha * np.exp(-n * LZ / pi)
    return (Rn ** 2) * (np.sin(theta) ** 2 + 0.01 * np.cos(n * theta))

# === GUI ===


class TensorBridgeGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Bridge Formula Tensor Visualizer")

        # n-slider
        self.n_slider = tk.Scale(root, from_=0, to=50, resolution=0.1, orient=tk.HORIZONTAL,
                                 label="n (Recursive Depth)", command=self.update_plot)
        self.n_slider.set(2)
        self.n_slider.pack(fill=tk.X, padx=10, pady=5)

        # Label to show current value
        self.value_label = tk.Label(root, text="S(n,θ) for n = 2.0")
        self.value_label.pack()

        # θ range
        self.theta_vals = np.linspace(0, 2 * np.pi, 400)

        # Matplotlib figure
        self.fig, self.ax = plt.subplots(figsize=(6, 4))
        self.canvas = FigureCanvasTkAgg(self.fig, master=root)
        self.canvas.get_tk_widget().pack()

        self.plot_tensor()

    def plot_tensor(self):
        n = self.n_slider.get()
        S_vals = angular_tensor(n, self.theta_vals)

        self.ax.clear()
        self.ax.plot(self.theta_vals, S_vals,
                     label=f"S(n,θ), n = {n:.2f}", color='navy')
        self.ax.set_title("Angular Tensor Stretching")
        self.ax.set_xlabel("θ (radians)")
        self.ax.set_ylabel("S(n, θ)")
        self.ax.grid(True)
        self.ax.legend()

        # Display current tensor range value
        max_val = np.max(S_vals)
        self.value_label.config(
            text=f"Max S(n,θ) at n = {n:.2f} → {max_val:.8e}")
        self.canvas.draw()

    def update_plot(self, event):
        self.plot_tensor()


# === Run GUI ===
if __name__ == "__main__":
    root = tk.Tk()
    app = TensorBridgeGUI(root)
    root.mainloop()
