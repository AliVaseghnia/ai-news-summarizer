import streamlit as st
from pymongo import MongoClient
import os
from dotenv import load_dotenv
from ingest import fetch_news
from summarize import generate_summaries
from datetime import datetime

load_dotenv()

# Connect to DB
client = MongoClient(os.getenv("MONGO_URI"))
db = client.news_db
summary_collection = db.summaries

# Custom CSS
st.markdown("""
    <style>
    .main-title {
        font-size: 3rem !important;
        font-weight: 700 !important;
        margin-bottom: 2rem !important;
    }
    .article-title {
        font-size: 1.2rem !important;
        font-weight: 600 !important;
        color: #2962FF !important;
        margin-bottom: 0.5rem !important;
    }
    .article-meta {
        font-size: 0.8rem !important;
        color: #666 !important;
        font-style: italic;
    }
    .article-summary {
        font-size: 1rem !important;
        line-height: 1.6 !important;
        margin: 1rem 0 !important;
    }
    .read-more {
        text-decoration: none !important;
        font-weight: 500 !important;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<h1 class="main-title">News Summarizer</h1>', unsafe_allow_html=True)

# Add dropdown for news categories
news_categories = [
    "technology", "business", "sports", "entertainment", 
    "science", "health", "politics", "world"
]
selected_category = st.selectbox(
    "Select news category",
    news_categories,
    index=0
)

# Single button for both operations
if st.button("Generate News Summaries"):
    with st.spinner(f"Fetching new articles for {selected_category}..."):
        fetch_news(query=selected_category)
    with st.spinner("Generating summaries..."):
        generate_summaries()
    st.success("News articles fetched and summarized successfully!")

st.markdown("### Latest News Articles")

# Fetch and display summaries
summaries = summary_collection.find().sort("publishedAt", -1).limit(10)
for summary in summaries:
    title = summary.get('title', 'Untitled Article')
    try:
        published_date = datetime.fromisoformat(summary['publishedAt'].replace('Z', '+00:00'))
        date_str = published_date.strftime('%B %d, %Y %I:%M %p')
    except:
        date_str = summary['publishedAt']
        
    with st.expander(f"{title}"):
        st.markdown(f'<div class="article-meta">Published by {summary["source"]} • {date_str}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="article-summary">{summary["summary"]}</div>', unsafe_allow_html=True)
        st.markdown(f'<a href="{summary["url"]}" target="_blank" class="read-more">Read full article →</a>', unsafe_allow_html=True)