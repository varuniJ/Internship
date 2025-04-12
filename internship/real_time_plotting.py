import matplotlib.pyplot as plt
import matplotlib.animation as animation
import serial
import joblib
import numpy as np
from PIL import Image
import os

# Load trained model and label encoder
model = joblib.load("svm_flex_sensor_model.pkl")
# Commented out because we're assuming model already returns string labels
# label_encoder = joblib.load("label_encoder.pkl")

# Serial port setup
ser = serial.Serial('COM4', 9600, timeout=1)

# Buffers for plotting
data_buffers = [[] for _ in range(5)]
time_buffer = []

# Set up the plot
fig, (ax, ax_img) = plt.subplots(1, 2, figsize=(12, 5))

# Line plots for each finger
lines = [ax.plot([], [], label=label)[0] for label in ['Thumb', 'Index', 'Middle', 'Ring', 'Pinky']]
ax.set_ylim(0, 1023)
ax.set_xlim(0, 100)
ax.legend()
ax.set_xlabel("Time (frames)")
ax.set_ylabel("Flex sensor value")

# Image display setup
img_display = ax_img.imshow(np.zeros((100, 100, 3), dtype=np.uint8))
ax_img.axis('off')
ax_img.set_title("Predicted Object")

# Update function for animation
def update(frame):
    line = ser.readline().decode('latin1').strip()
    print(f"🔍 Raw line from serial: {line}")

    parts = line.split(',')

    if len(parts) == 5:
        try:
            values = [int(val) for val in parts]

            # Real-time plotting
            for i, val in enumerate(values):
                data_buffers[i].append(val)
                if len(data_buffers[i]) > 100:
                    data_buffers[i].pop(0)

            time_buffer.append(frame)
            if len(time_buffer) > 100:
                time_buffer.pop(0)

            for i, line in enumerate(lines):
                line.set_data(range(len(data_buffers[i])), data_buffers[i])

            # Prediction
            input_data = np.array(values).reshape(1, -1)
            predicted_label = model.predict(input_data)[0]  # Removed inverse_transform
            print(f"🎯 Predicted Object: {predicted_label}")

            # Update image
            img_path = f"{predicted_label}.jpg"
            if os.path.exists(img_path):
                img = Image.open(img_path)
                img_display.set_data(img)
                ax_img.set_title(f"Predicted: {predicted_label}")
            else:
                ax_img.set_title(f"Image not found for: {predicted_label}")
        except ValueError:
            print("⚠️ Invalid sensor data")
    else:
        print("⚠️ Invalid format")

    return lines + [img_display]

# Animate
ani = animation.FuncAnimation(fig, update, interval=300)
plt.tight_layout()
plt.show()
