import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image

# Load CSV with sensor data + prediction
df = pd.read_csv("combined.csv")

# Plot sensor data
plt.figure(figsize=(12, 6))
for col in df.columns[:-1]:  # exclude last column (prediction)
    plt.plot(df.index, df[col], label=col)

plt.xlabel("Sample Index")
plt.ylabel("Sensor Reading")
plt.title("Sensor Data from Real-Time Capture")
plt.legend()

# Show the plot
plt.tight_layout()
plt.show()

# Get the final predicted object
last_prediction = df.iloc[-1, -1]  # last row, last column

# Map predicted label to image
object_images = {
    "sphere": "sphere.jpg",
    "cylinder": "cylinder.jpg",
    "cuboid": "cuboid.jpg"
}

# Load and show the image
if last_prediction in object_images:
    img = Image.open(object_images[last_prediction])
    img.show()
else:
    print(f"No image found for prediction: {last_prediction}")
