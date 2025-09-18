# CORD-19 Data Explorer  

An interactive **Streamlit web app**
link to app - https://frameworksassignment-p2jvcgezrudkvtqtmtg4ru.streamlit.app/
For exploring COVID-19 research papers from the https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge  
The app loads metadata, cleans it, and provides interactive visualizations of publication trends, top journals, frequent words, and more.  

---

## 🚀 Features
- **Data loading & cleaning**
  - Handles missing values
  - Converts dates & extracts publication years
  - Computes abstract word counts  

- **Exploratory analysis**
  - Number of publications over time  
  - Top journals publishing COVID-19 research  
  - Most frequent words in titles (via word cloud)  
  - Distribution of papers by source  

- **Interactive Streamlit app**
  - Year range slider filter  
  - Auto-updating charts & tables  
  - Word cloud visualization  
  - Sample of filtered data  

---

## 🛠️ Tech Stack
- [Streamlit](https://streamlit.io/) – interactive app  
- [Pandas](https://pandas.pydata.org/) – data handling  
- [Matplotlib](https://matplotlib.org/) / [Seaborn](https://seaborn.pydata.org/) – visualizations  
- [WordCloud](https://amueller.github.io/word_cloud/) – word cloud generation  

---

## 📂 Project Structure
├── app.py # Main Streamlit app
|--cors19.py # python file with data analysis.
├── metadata_sample.csv # Sample dataset (CORD-19 metadata subset)
├── requirements.txt # Dependencies
└── README.md # Project documentation
---

## ⚡ Quickstart

### Run Locally
```bash
# 1. Clone repo
# 2. Install dependencies
pip install -r requirements.txt

# 3. Run app
streamlit run app.py
The app will open in your browser at http://localhost:8501.

Run on Streamlit Cloud

Push this repo to GitHub.

Go to Streamlit Cloud
.

Deploy new app → select repo & app.py.

Done 🎉 → You’ll get a public URL like:

https://<your-username>-cord19-explorer.streamlit.app

📊 Example Visualizations

Bar chart of publications over time

Top 10 publishing journals

Word cloud of paper titles

Distribution of papers by source

✨ Reflection

This project demonstrates how to:

Load, clean, and explore real-world scientific metadata

Use Streamlit for rapid prototyping of interactive dashboards

Visualize key research insights with minimal code

🔮 Future Work

Natural Language Processing (NLP):
Apply topic modeling (e.g., LDA, BERTopic) on abstracts to uncover research themes.

Trend Forecasting:
Use time-series models to forecast future research publication trends.

Network Analysis:
Explore co-authorship and citation networks.

Interactive Filters:
Add more filters (author, journal, keywords) to improve interactivity.

Scalability:
Connect directly to larger datasets (full CORD-19) via APIs or cloud storage
