# 🔐 AI-Based Phishing URL Detection System

An AI + Cyber Security project that detects phishing websites using a **Random Forest classifier** trained on a real-world dataset of URLs.  
The system predicts whether a website is **Legitimate (0)** or **Phishing (1)** with high accuracy (~91%).

---

## ⚙️ How to Run

### Step 1: Clone the Repository
```bash
1.git clone https://github.com/Praveen314-oss/ChaosPhishGuard.git
2.cd ChaosPhishGuard
Step 2: Install Dependencies
3.pip install -r requirements.txt
Step 3: Train the Phishing Detection Model
Run the training script to train the model and save it:
4.python phish_detector.py
Expected Output:
Accuracy: ~91%
Model trained and saved successfully!
Step 4: Predict a URL
Run the prediction script to test new URLs:
5.python predict_url.py
Example Input & Output:
Enter website URL: http://secure-login-paypal.verify-user.com
Prediction: Phishing (1)
Enter website URL: https://www.google.com
Prediction: Legitimate (0)

📌 Project Description
This project uses machine learning to automatically detect phishing websites.
It extracts URL-based features and classifies them as Legitimate (0) or Phishing (1) using a Random Forest model.

The model is trained on a real-world dataset of over 115,000 URLs and achieves around 91% accuracy.
The system is simple to use and can predict new URLs in real-time.

💡 My Contributions
Designed the feature extraction function for URLs.

Created the interactive URL prediction script with real-time input.

Integrated feature extraction with the trained Random Forest model.

Displayed clear results: Phishing (1) or Legitimate (0).

Handled dataset preprocessing and trained the model on a real-world dataset.

Note: Some parts of the training and prediction scripts were generated with AI assistance (ChatGPT), and I adapted and executed them for this project.

📂 Project Structure
bash
Copy code
AI-Phishing-URL-Detection/
│
├── phishing.csv           # Dataset of URLs and labels
├── phish_detector.py      # Model training script
├── predict_url.py         # URL prediction script
├── phishing_model.pkl     # Saved trained model
├── requirements.txt       # Required Python libraries
└── README.md              # Project documentation
🧰 Technologies Used
Python

Pandas

Scikit-learn

Joblib

Random Forest Classifier

📈 Model Performance
Algorithm: Random Forest Classifier

Accuracy: ~91%

Type: Supervised Machine Learning




