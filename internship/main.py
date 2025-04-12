import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt
import joblib

# Step 1: Load the original dataset
original_data = pd.read_csv("combined.csv", header=None)
X = original_data.iloc[:, :-1]
y = original_data.iloc[:, -1]

# Step 2: Augment dataset with noise
def augment_data(X, y, n_copies=3, noise_level=10):
    X_aug = []
    y_aug = []

    for _ in range(n_copies):
        noise = np.random.normal(0, noise_level, X.shape)
        X_noisy = X + noise
        X_aug.append(X_noisy)
        y_aug.append(y.copy())

    X_all = pd.concat([X] + X_aug, ignore_index=True)
    y_all = pd.concat([y] + y_aug, ignore_index=True)
    return X_all, y_all

X_aug, y_aug = augment_data(X, y, n_copies=3, noise_level=10)

# Step 3: Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X_aug, y_aug, test_size=0.2, random_state=42, stratify=y_aug)

# Step 4: Train SVM
clf = SVC(kernel='linear')
clf.fit(X_train, y_train)

# Step 5: Predict
y_pred = clf.predict(X_test)

# Step 6: Accuracy and Report
accuracy = accuracy_score(y_test, y_pred)
print(f"SVM Accuracy: {accuracy * 100:.2f}%\n")
print("Classification Report:\n", classification_report(y_test, y_pred))

# Step 7: Confusion Matrix
labels = sorted(y.unique())  # Maintain label order
cm = confusion_matrix(y_test, y_pred, labels=labels)
cm_percentage = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis] * 100

# Annotate with both percentage and count
annot = np.empty_like(cm).astype(str)
for i in range(cm.shape[0]):
    for j in range(cm.shape[1]):
        percentage = cm_percentage[i, j]
        count = cm[i, j]
        annot[i, j] = f'{percentage:.1f}%\n{count}'

# Plot heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(cm_percentage, annot=annot, fmt='', cmap='viridis',
            xticklabels=labels, yticklabels=labels, cbar=True)
plt.xlabel('Predicted label')
plt.ylabel('True label')
plt.title(f'SVM Accuracy: {accuracy * 100:.2f}%')
plt.tight_layout()
plt.show()

# Step 8: Save model
joblib.dump(clf, "svm_flex_sensor_model.pkl")
print("\n✅ Model saved as svm_flex_sensor_model.pkl")
