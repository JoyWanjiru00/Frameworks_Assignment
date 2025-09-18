# app.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

st.set_page_config(page_title="CORD-19 Data Explorer", layout="wide")
st.title("CORD-19 Data Explorer")
st.write("Interactive exploration of COVID-19 research papers")

# ==== Load Data ====
@st.cache_data
def load_data():
    # Load local CSV (make sure it's in the repo)
    df = pd.read_csv("metadata_sample.csv", low_memory=False)
    df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')
    df['year'] = df['publish_time'].dt.year
    return df

df = load_data()

# ==== Sidebar filters ====
st.sidebar.header("Filters")
year_min, year_max = int(df['year'].min()), int(df['year'].max())
year_range = st.sidebar.slider("Select year range", year_min, year_max, (year_min, year_max))
mask = df['year'].between(year_range[0], year_range[1])
subset = df[mask]

# ==== Publications Over Time ====
st.subheader("Publications Over Time")
year_counts = subset['year'].value_counts().sort_index()
st.bar_chart(year_counts)

# ==== Top Journals ====
st.subheader("Top Journals")
top_journals = subset['journal'].value_counts().head(10)
fig, ax = plt.subplots(figsize=(8, 5))
top_journals.plot(kind="barh", ax=ax, color="skyblue")
ax.set_title("Top 10 Journals")
st.pyplot(fig)

# ==== Word Cloud ====
st.subheader("Word Cloud of Paper Titles")
text = " ".join(subset['title'].dropna().astype(str))
if text.strip():
    wordcloud = WordCloud(width=800, height=400, background_color="white").generate(text)
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.imshow(wordcloud, interpolation="bilinear")
    ax.axis("off")
    st.pyplot(fig)
else:
    st.write("⚠️ No titles available for this filter.")

# ==== Source Distribution ====
if "source_x" in subset.columns:
    st.subheader("Top Sources")
    top_sources = subset['source_x'].value_counts().head(10)
    fig, ax = plt.subplots(figsize=(8, 5))
    top_sources.plot(kind="bar", ax=ax, color="orange")
    ax.set_title("Top 10 Sources")
    st.pyplot(fig)

# ==== Show Sample Data ====
st.subheader("Sample of Filtered Data")
st.write(subset.head())
