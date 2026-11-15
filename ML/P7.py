import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import LinearSVC
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report
)

# Load dataset
data = pd.read_csv("emails.csv")

# Separate input and output
X = data.drop(["Email No.", "Prediction"], axis=1)
y = data["Prediction"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Scale data for KNN
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Create KNN model
knn = KNeighborsClassifier(n_neighbors=5)

# Create SVM model
svm = LinearSVC(max_iter=5000, random_state=42)

# Train models
knn.fit(X_train_scaled, y_train)
svm.fit(X_train, y_train)

# Make predictions
knn_pred = knn.predict(X_test_scaled)
svm_pred = svm.predict(X_test)

# KNN Performance
print("\nKNN Performance")
print("Accuracy:", accuracy_score(y_test, knn_pred))
print("Confusion Matrix:")
print(confusion_matrix(y_test, knn_pred))
print(classification_report(
    y_test, knn_pred,
    target_names=["Normal", "Spam"],
    zero_division=0
))

# SVM Performance
print("\nSVM Performance")
print("Accuracy:", accuracy_score(y_test, svm_pred))
print("Confusion Matrix:")
print(confusion_matrix(y_test, svm_pred))
print(classification_report(
    y_test, svm_pred,
    target_names=["Normal", "Spam"],
    zero_division=0
))


# -----------------------------------------
# SAMPLE INPUT:
# Dataset: emails.csv
# No manual input required.
#
# SAMPLE OUTPUT:
#
# KNN Performance
# Accuracy: (Calculated value)
# Confusion Matrix:
# [[... ...]
#  [... ...]]
#
# SVM Performance
# Accuracy: (Calculated value)
# Confusion Matrix:
# [[... ...]
#  [... ...]]
#
# Classification Report:
# Precision, Recall and F1-score
# for Normal and Spam classes.
#
# INSTALL:
# python -m pip install pandas scikit-learn
#
# RUN:
# python P7.py
# -----------------------------------------
