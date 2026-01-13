import pandas as pd
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

from utils.text_cleaner import clean_text

# Load dataset
df = pd.read_csv("data/resume_dataset.csv")

# Clean resume text
df["cleaned_resume"] = df["Resume"].apply(clean_text)

# Features & labels
X = df["cleaned_resume"]
y = df["Category"]


# TF-IDF Vectorizer
tfidf = TfidfVectorizer(max_features=3000)
X_tfidf = tfidf.fit_transform(X)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X_tfidf, y, test_size=0.2, random_state=42
)

# Train model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print("Model Accuracy:", accuracy)

# Save model & vectorizer
with open("model/job_model.pkl", "wb") as f:
    pickle.dump(model, f)

with open("model/tfidf.pkl", "wb") as f:
    pickle.dump(tfidf, f)
