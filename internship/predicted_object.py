import pandas as pd
import matplotlib.pyplot as plt

# Assign proper column names (in same order as sensor values)
columns = ["Thumb", "Index", "Middle", "Ring", "Pinky"]

cuboid_df = pd.read_csv("cuboid.csv", names=columns)
cylinder_df = pd.read_csv("cylinder.csv", names=columns)
sphere_df = pd.read_csv("sphere.csv", names=columns)

df = pd.read_csv("combined.csv", header=1)  # or header=None depending on your file

# Rename columns appropriately
df.columns = ['Sensor1', 'Sensor2', 'Sensor3', 'Sensor4', 'Sensor5', 'Predicted_Object']

# Plot sensor readings
plt.figure(figsize=(10, 6))
for col in df.columns[:-1]:  # Exclude 'Predicted_Object'
    plt.plot(df.index, df[col], label=col)

predicted_object = df["Predicted_Object"].mode()
print("Predicted Object:", predicted_object)
plt.title(f"Sensor Data (Predicted Object: {predicted_object})")
plt.xlabel("Sample Index")
plt.ylabel("Sensor Reading (V)")
plt.title("Sensor Data from Real-Time Capture")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

