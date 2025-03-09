import streamlit as st
import pandas as pd
import plotly.express as px
from sentiment import analyze_sentiment
from news_fetcher import get_news
import os
from dotenv import load_dotenv

load_dotenv()

# Configure Streamlit
st.set_page_config(page_title="Sentiment Analysis Dashboard", layout="wide")
st.title("📰 Real-Time Sentiment Analysis of News Headlines")

# Sidebar input
keyword = st.sidebar.text_input("Enter a keyword (e.g., 'AI', 'Bitcoin'):", "technology")

# Fetch and analyze news
articles = get_news(keyword)

if not articles:
    st.error("Failed to fetch news. Check your API key or internet connection.")
else:
    # Analyze sentiments
    sentiments = []
    for article in articles:
        label, score = analyze_sentiment(article['title'])
        sentiments.append({
            'Sentiment': label,
            'Confidence': round(score, 2),
            **article
        })

    df = pd.DataFrame(sentiments)

    # Display data
    st.subheader(f"Latest News for '{keyword}'")
    st.dataframe(df)

    # Visualizations
    col1, col2 = st.columns(2)
    with col1:
        fig1 = px.pie(df, names='Sentiment', title='Sentiment Distribution')
        st.plotly_chart(fig1)
    with col2:
        fig2 = px.bar(df, x='source', y='Confidence', color='Sentiment', title='Sentiment by Source')
        st.plotly_chart(fig2)