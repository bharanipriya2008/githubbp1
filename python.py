import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score, classification_report


# Sample dataset
data = {
    "message": [
        "Congratulations! You won a free lottery ticket",
        "Win cash now! Click this link to claim your prize",
        "Free entry in our contest, reply WIN",
        "You have won a $1000 gift voucher",
        "Claim your free reward now",
        "URGENT! You have won a prize",
        "Get free money by clicking this link",

        "Hi, how are you?",
        "Can we meet tomorrow?",
        "Please send me the project file",
        "Your appointment is confirmed",
        "Don't forget to attend the meeting",
        "Happy birthday! Have a great day",
        "Can you call me when you are free?",
    ],
    "label": [
        "spam",
        "spam",
        "spam",
        "spam",
        "spam",
        "spam",
        "spam",

        "ham",
        "ham",
        "ham",
        "ham",
        "ham",
        "ham",
        "ham"
    ]
}

# Create DataFrame
df = pd.DataFrame(data)

# Separate input and output
X = df["message"]
y = df["label"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42
)

# Create machine learning pipeline
model = Pipeline([
    ("tfidf", TfidfVectorizer()),
    ("classifier", MultinomialNB())
])

# Train the model
model.fit(X_train, y_train)

# Test the model
y_pred = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)

print("Model Accuracy:", round(accuracy * 100, 2), "%")
print("\nClassification Report:")
print(classification_report(y_test, y_pred, zero_division=0))


# Function to detect spam
def detect_spam(message):
    prediction = model.predict([message])[0]

    if prediction == "spam":
        return "SPAM MESSAGE"
    else:
        return "NOT SPAM"


# Test user messages
print("\n--- Spam Message Detector ---")

while True:
    message = input("\nEnter a message (or type 'exit' to quit): ")

    if message.lower() == "exit":
        print("Program closed.")
        break

    result = detect_spam(message)

    print("Result:", result)
  
