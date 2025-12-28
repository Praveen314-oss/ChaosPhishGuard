# ===============================
# Phishing URL Prediction Script
# ===============================

import joblib

# Step 1: Load the trained model

model = joblib.load("phishing_model.pkl")


# Step 2: Define feature extraction

def extract_features(url):
  
    features = []
    features.append(len(url))                     # URL length
    features.append(url.count('.'))              # Number of dots
    features.append(1 if '@' in url else 0)     # '@' symbol
    features.append(1 if '-' in url else 0)     # Hyphen
    features.append(1 if url.startswith("https") else 0)  # HTTPS
    return features


# Step 3: URL prediction loop

print("\n--- Phishing URL Prediction ---")
print("Type 'exit' to quit.\n")

while True:
    url = input("Enter website URL: ")
    if url.lower() == "exit":
        print("Exiting program...")
        break

# Extract features and predict
    features = extract_features(url)
    prediction = model.predict([features])[0]

# Display result
    if prediction == 1:
        print("Prediction: Phishing (1)")
    else:
        print("Prediction: Legitimate (0)")
