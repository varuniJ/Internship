import pandas as pd

sphere = pd.read_csv("sphere.csv", header=None)
cuboid = pd.read_csv("cuboid.csv", header=None)
cylinder = pd.read_csv("cylinder.csv", header=None)

# Add labels
sphere['label'] = 'sphere'
cuboid['label'] = 'cuboid'
cylinder['label'] = 'cylinder'

# Combine
combined = pd.concat([sphere, cuboid, cylinder], ignore_index=True)

# Save
combined.to_csv("combined.csv", index=False, header=False)

