# Email Spam Detection: KNN vs SVM
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# read data
df = pd.read_csv("emails.csv")
print(df.shape)
print(df["Prediction"].value_counts())      # 0 = Not Spam, 1 = Spam

# features and target
X = df.drop(["Email No.", "Prediction"], axis=1)
y = df["Prediction"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

# ---------- KNN ----------
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)
knn_pred = knn.predict(X_test)

# ---------- SVM ----------
svm = SVC(kernel="linear")
svm.fit(X_train, y_train)
svm_pred = svm.predict(X_test)

# ---------- Results ----------
print("\n===== KNN =====")
print("Accuracy:", accuracy_score(y_test, knn_pred))
print(confusion_matrix(y_test, knn_pred))
print(classification_report(y_test, knn_pred))

print("\n===== SVM =====")
print("Accuracy:", accuracy_score(y_test, svm_pred))
print(confusion_matrix(y_test, svm_pred))
print(classification_report(y_test, svm_pred))

if accuracy_score(y_test, svm_pred) > accuracy_score(y_test, knn_pred):
    print("\nSVM performed better")
else:
    print("\nKNN performed better")


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
