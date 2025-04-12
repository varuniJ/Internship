import serial
import joblib
import numpy as np

model = joblib.load("svm_flex_sensor_model.pkl")
ser = serial.Serial("COM4", 9600, timeout=0.2)
ser.flushInput()

print("📡 Starting real-time prediction...")

while True:
    try:
        line = ser.readline().decode('utf-8').strip()
        data = line.split(',')

        if len(data) == 5:
            sample = np.array([int(val) for val in data]).reshape(1, -1)
            prediction = model.predict(sample)
            print("🎯 Predicted Object:", prediction[0])
        else:
            print(f"❌ Invalid data received: {data}")

    except Exception as e:
        print("⚠️ Error:", e)
