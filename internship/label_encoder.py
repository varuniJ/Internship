import pandas as pd
from sklearn.svm import SVC
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib

# Load and prepare the data
df = pd.read_csv("combined.csv", header=None)
df.columns = ['pinky', 'ring', 'middle', 'index', 'thumb', 'label']

# Encode labels
le = LabelEncoder()
df['label_encoded'] = le.fit_transform(df['label'])

# Features and labels
X = df[['pinky', 'ring', 'middle', 'index', 'thumb']]
y = df['label_encoded']

# Split data for training and testing (optional but good for evaluation)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train SVM
model = SVC(kernel='rbf', C=1, gamma='scale')
model.fit(X_train, y_train)

# Test accuracy (optional but useful)
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))

# Save model and label encoder
#joblib.dump(model, "svm_model.pkl")
joblib.dump(le, "label_encoder.pkl")

print("✅  Label Encoder saved successfully!")
