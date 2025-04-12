import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.image import imread

# === Load CSV files ===
cuboid_df = pd.read_csv("cuboid.csv", names=["Thumb", "Index", "Middle", "Ring", "Pinky"])
cylinder_df = pd.read_csv("cylinder.csv", names=["Thumb", "Index", "Middle", "Ring", "Pinky"])
sphere_df = pd.read_csv("sphere.csv", names=["Thumb", "Index", "Middle", "Ring", "Pinky"])

# === Normalize to Voltage (assuming 3.3V ADC reference) ===
cuboid_df = cuboid_df / 1023.0 * 3.3
cylinder_df = cylinder_df / 1023.0 * 3.3
sphere_df = sphere_df / 1023.0 * 3.3

# === Load object images ===
cuboid_img = imread("cuboid.jpg")     # Replace with your actual file paths
cylinder_img = imread("cylinder.jpg")
sphere_img = imread("sphere.jpg")

# === Create subplots ===
fig, axs = plt.subplots(2, 3, figsize=(15, 8))
colors = ['black', 'red', 'blue', 'green', 'purple']
labels = ["Thumb", "Index", "Middle", "Ring", "Pinky"]

def plot_graph(ax, df, title, img):
    for i, label in enumerate(labels):
        ax.plot(df.index / 50.0, df[label], color=colors[i], label=label)  # assuming 50Hz
    ax.set_title(title)
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Voltage (V)")
    ax.set_ylim(0, 1.5)
    ax.legend()

# === Plot sensor data ===
plot_graph(axs[0, 0], cuboid_df, "(a) Cuboid", cuboid_img)
plot_graph(axs[0, 1], cylinder_df, "(b) Cylinder", cylinder_img)
plot_graph(axs[0, 2], sphere_df, "(c) Sphere", sphere_img)

# === Show object images ===
axs[1, 0].imshow(cuboid_img)
axs[1, 1].imshow(cylinder_img)
axs[1, 2].imshow(sphere_img)
for ax in axs[1]: ax.axis("off")

plt.tight_layout()
plt.show()
