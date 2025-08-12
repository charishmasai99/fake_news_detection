"""
Fake News Detection - Python Script
------------------------------------
This script uses Logistic Regression + TF-IDF to classify news as REAL or FAKE.
Dataset: Fake.csv & True.csv (provided by user)
"""

# STEP 1: Import libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import pandas as pd
df_fake = pd.read_csv("Fake.csv", encoding="utf-8")
df_true = pd.read_csv("True.csv", encoding="utf-8")


# STEP 3: Label data (0 = Fake, 1 = Real)
df_fake["label"] = 0
df_true["label"] = 1

# STEP 4: Combine datasets and shuffle
df = pd.concat([df_fake, df_true], ignore_index=True)
df = df.sample(frac=1, random_state=42).reset_index(drop=True)

# STEP 5: Clean missing values & combine title + text
df["title"] = df["title"].fillna("")
df["text"] = df["text"].fillna("")
df["content"] = df["title"] + " " + df["text"]

# STEP 6: Features (X) and labels (y)
X = df["content"]
y = df["label"]

# STEP 7: Train/test split
print("Splitting dataset...")
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, stratify=y, random_state=42
)

# STEP 8: TF-IDF Vectorization
print("Vectorizing text...")
vectorizer = TfidfVectorizer(stop_words="english", max_df=0.7)
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# STEP 9: Train Logistic Regression model
print("Training model...")
model = LogisticRegression(max_iter=1000, random_state=42)
model.fit(X_train_vec, y_train)

# STEP 10: Evaluate
y_pred = model.predict(X_test_vec)
print("\nModel Evaluation:")
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))

# STEP 11: Predict function
def predict_news(news_text):
    vec = vectorizer.transform([news_text])
    pred = model.predict(vec)[0]
    return "REAL" if pred == 1 else "FAKE"

# STEP 12: Test prediction
sample_text = "The president announced new measures for economic growth."
print("\nSample Prediction:", predict_news(sample_text))
import pickle


import pickle

# Save model
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

# Save vectorizer
with open("vectorizer.pkl", "wb") as f:
    pickle.dump(vectorizer, f)
