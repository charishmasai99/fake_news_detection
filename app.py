import streamlit as st
import joblib

# -------------------------------
# Step 1: Load trained model & vectorizer
# -------------------------------
model = joblib.load("model.pkl")        # Replace with your model filename
vectorizer = joblib.load("vectorizer.pkl")        # Replace with your vectorizer filename

# -------------------------------
# Step 2: App title & description
# -------------------------------
st.set_page_config(page_title="📰 Fake News Detection", page_icon="📰", layout="centered")

st.title("📰 Fake News Detection")
st.write("Paste a news headline or article below to check if it's **real** or **fake**.")

# -------------------------------
# Step 3: User input
# -------------------------------
news_text = st.text_area("Enter News Text", height=200)

# -------------------------------
# Step 4: Prediction logic
# -------------------------------
if st.button("Check News"):
    if news_text.strip():
        # Convert the input into numerical features
        vectorized_text = vectorizer.transform([news_text])

        # Get prediction (0 = fake, 1 = real)
        prediction = model.predict(vectorized_text)[0]

        # Get confidence score
        proba = model.predict_proba(vectorized_text)[0]
        confidence = max(proba) * 100

        # Display result
        if prediction == 1:
            st.success(f"✅ This news is likely REAL.\nConfidence: {confidence:.2f}%")
        else:
            st.error(f"🚨 This news is likely FAKE.\nConfidence: {confidence:.2f}%")

    else:
        st.warning("⚠️ Please enter some text before checking.")

# -------------------------------
# Footer
# -------------------------------
st.markdown("---")
st.caption("Built with ❤️ using Streamlit & Machine Learning")
