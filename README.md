# 📰 Fake News Detection

A machine learning project that detects whether a news article is **Fake** or **True** based on its content.

##📌 Features
- Preprocesses news headlines and articles.
- Uses a trained ML model (`model.pkl`) and vectorizer (`vectorizer.pkl`).
- Classifies input text as **FAKE** or **REAL**.
- Built with **Python**, **scikit-learn**, and **Flask**.

## 📂 ```Project Structure
fake_news_detection/
│-- app.py # Web application script
│-- main.py # Main ML training/testing script
│-- Fake.csv # Dataset of fake news articles
│-- True.csv # Dataset of real news articles
│-- model.pkl # Trained model
│-- vectorizer.pkl # Text vectorizer
│-- requirements.txt # Python dependencies

## 📊 Dataset
- **Fake.csv** → Contains fake news articles.
- **True.csv** → Contains real news articles.
> Note: Files are large (>50MB) and stored in this repository.  
> You can also use the [Kaggle Fake News Dataset](https://www.kaggle.com/clmentbisaillon/fake-and-real-news-dataset).

## ⚙️ Installation
1. Clone the repository:
```bash
git clone https://github.com/charishmasai99/fake_news_detection.git
cd fake_news_detection
Install dependencies:

```bash
Copy code
pip install -r requirements.txt
🚀 Usage
Run the Flask app:

```bash
Copy code
python app.py
Then open http://127.0.0.1:5000 in your browser.

##📈 Model
Algorithm: Logistic Regression / Naive Bayes (based on your training choice)

Vectorization: TF-IDF

Accuracy: ~XX% (replace with your actual score)

##🛠 Technologies Used
Python

Pandas, NumPy

Scikit-learn

Flask

HTML/CSS (for UI)
## 📸 Demo
![Fake News Detection Demo](demopic.png)
![Fake News Detection Demo](demopicfake.png)
##📌 Future Improvements
Deploy online using Heroku/Render/Streamlit.

Add real-time news scraping.

Enhance preprocessing with advanced NLP.

##🤝 Contributing
Pull requests are welcome. For major changes, open an issue first to discuss your ideas.


