import pandas as pd

# Load the CSV without assuming headers
df = pd.read_csv("combined.csv", header=None)

# Rename columns correctly
df.columns = ['pinky', 'ring', 'middle', 'index', 'thumb', 'label']

# Now you can safely use the data
print(df.head())
print(df['label'].value_counts())  # Show class distribution
