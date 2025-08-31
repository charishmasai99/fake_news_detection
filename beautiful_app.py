import streamlit as st
import pickle

# Load trained model + vectorizer
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

themes = {
    "Neon 🌈": """
        body, .stApp {
            background: linear-gradient(135deg, #ff6a00, #ee0979);
            background-attachment: fixed;
        }
    """,
    "Ocean 🌊": """
        body, .stApp {
            background: linear-gradient(135deg, #2193b0, #6dd5ed);
            background-attachment: fixed;
        }
    """,
    "Sunset 🌅": """
        body, .stApp {
            background: linear-gradient(135deg, #f7971e, #ffd200);
            background-attachment: fixed;
        }
    """,
    "Forest 🌿": """
        body, .stApp {
            background: linear-gradient(135deg, #134e5e, #71b280);
            background-attachment: fixed;
        }
    """,
    "Galaxy 🌌": """
        body, .stApp {
            background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
            background-attachment: fixed;
        }
    """,
    "Candy 🍭": """
        body, .stApp {
            background: linear-gradient(135deg, #ff9a9e, #fad0c4);
            background-attachment: fixed;
        }
    """,
    "Royal 💜": """
        body, .stApp {
            background: linear-gradient(135deg, #654ea3, #eaafc8);
            background-attachment: fixed;
        }
    """,
    "Fire 🔥": """
        body, .stApp {
            background: linear-gradient(135deg, #f12711, #f5af19);
            background-attachment: fixed;
        }
    """,
}


# 🌟 Glassmorphism + Styling
glass_css = """
    /* Sidebar glass */
    section[data-testid="stSidebar"] {
        background: rgba(255, 255, 255, 0.15) !important;
        backdrop-filter: blur(15px) !important;
        border-radius: 15px;
    }

    /* Textbox */
    textarea {
        background: rgba(255, 255, 255, 0.2) !important;
        backdrop-filter: blur(10px) !important;
        border-radius: 15px !important;
        padding: 10px;
        font-size: 16px;
    }

    /* Buttons */
    div.stButton > button {
        background: linear-gradient(to right, #ff758c, #ff7eb3) !important;
        color: white !important;
        border-radius: 25px !important;
        padding: 0.6em 1.5em !important;
        border: none;
        font-weight: bold;
        box-shadow: 0 4px 15px rgba(255, 118, 150, 0.4);
        transition: 0.3s ease-in-out;
    }
    div.stButton > button:hover {
        transform: scale(1.05);
        box-shadow: 0 6px 20px rgba(255, 118, 150, 0.6);
    }

    /* Titles */
    .main-title {
        font-size: 42px;
        font-weight: 800;
        text-align: center;
        color: #fff;
        margin-bottom: 20px;
        text-shadow: 2px 2px 6px rgba(0,0,0,0.3);
    }
    .sub-title {
        font-size: 18px;
        text-align: center;
        color: #fff;
        margin-bottom: 30px;
    }

    /* Result box */
    .result-box {
        padding: 20px;
        border-radius: 15px;
        text-align: center;
        font-size: 22px;
        font-weight: bold;
        margin-top: 25px;
        background: rgba(255, 255, 255, 0.2);
        backdrop-filter: blur(12px);
        color: #fff;
        box-shadow: 0 4px 25px rgba(0,0,0,0.3);
    }
"""

# 🌟 Prediction Glow
prediction_box_css = """
    .prediction-card {
        background: rgba(255, 255, 255, 0.2);
        backdrop-filter: blur(12px);
        border-radius: 20px;
        padding: 20px;
        margin-top: 20px;
        text-align: center;
        font-size: 22px;
        font-weight: bold;
        color: white;
        box-shadow: 0 4px 30px rgba(0, 0, 0, 0.3);
        animation: glow 3s infinite alternate;
    }

    @keyframes glow {
        0% { box-shadow: 0 0 15px #ff758c, 0 0 30px #ff7eb3; }
        50% { box-shadow: 0 0 20px #42e695, 0 0 40px #3bb2b8; }
        100% { box-shadow: 0 0 15px #6a11cb, 0 0 30px #2575fc; }
    }
"""

# --- Theme Selector ---
selected_theme = st.sidebar.selectbox("🌸 Choose Theme", list(themes.keys()))

# Apply CSS
st.markdown(f"<style>{themes[selected_theme]} {glass_css} {prediction_box_css}</style>", unsafe_allow_html=True)

# --- APP CONTENT ---
st.markdown("<div class='main-title'>📰 Fake News Detector</div>", unsafe_allow_html=True)
st.markdown("<div class='sub-title'>Switch between pastel, neon, or galaxy mode ✨</div>", unsafe_allow_html=True)

news_text = st.text_area("✍️ Enter News Article Below:", height=180)

if st.button("🔍 Analyze"):
    if news_text.strip() == "":
        st.warning("⚠️ Please enter some text first.")
    else:
        transformed_text = vectorizer.transform([news_text])
        prediction = model.predict(transformed_text)[0]
        if prediction == 0:
            st.markdown("<div class='result-box' style='background: linear-gradient(135deg, #a1ffce, #faffd1); color:#333;'>✅ This news is REAL</div>", unsafe_allow_html=True)
        else:
            st.markdown("<div class='result-box' style='background: linear-gradient(135deg, #ffdde1, #ee9ca7); color:#333;'>❌ This news is FAKE</div>", unsafe_allow_html=True)
