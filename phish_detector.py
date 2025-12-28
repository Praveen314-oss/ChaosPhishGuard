# ==========================================
# AI-Based Phishing URL Detection - Training
# ==========================================

import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score


# Step 1: Load the dataset

# The dataset contains URLs and labels (0 = Legitimate, 1 = Phishing)
data = pd.read_csv("phishing.csv")


# Step 2: Define feature extraction

def extract_features(url):

    features = []
    features.append(len(url))                      # URL length
    features.append(url.count('.'))                # Number of dots in the URL
    features.append(1 if '@' in url else 0)       # Presence of '@' symbol
    features.append(1 if '-' in url else 0)       # Presence of hyphen
    features.append(1 if url.startswith("https") else 0)  # HTTPS usage
    return features


# Step 3: Prepare data for ML

X = data['url'].apply(extract_features).tolist()  # Features
y = data['label']                                  # Target labels

# Split dataset into training and testing sets 
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


# Step 4: Train Random Forest model

model = RandomForestClassifier()
model.fit(X_train, y_train)


# Step 5: Evaluate model accuracy

predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)
print(f"Accuracy: {accuracy:.4f}")


# Step 6: Save trained model

joblib.dump(model, "phishing_model.pkl")
print("Model trained and saved successfully!")
