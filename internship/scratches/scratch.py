import serial
import csv
import time

# Open serial port (adjust COM port as needed)
ser = serial.Serial('COM4', 9600, timeout=1)
time.sleep(2)  # Wait for connection to establish

# Open CSV file to write
with open("../../../../../Downloads/internship/sphere.csv", mode="w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file)

    print("🔄 Starting Data Collection...")

    for sample_num in range(200):
        line = ser.readline().decode('latin1').strip()
        data = line.split(',')

        if len(data) == 5:
            try:
                row = [int(val.strip()) for val in data]
                writer.writerow(row)
                print(f"✅ Sample {sample_num+1}/200 saved.")
            except ValueError:
                print(f"❌ Could not parse values: {data}")
        else:
            print(f"⚠️ Invalid data format: {data}")

print("✅ Data collection complete! File saved as: sphere.csv")
