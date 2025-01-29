import streamlit as st
from pymongo import MongoClient
import os
from dotenv import load_dotenv
from ingest import fetch_news
from summarize import generate_summaries

load_dotenv()

# Connect to DB
client = MongoClient(os.getenv("MONGO_URI"))
db = client.news_db
summary_collection = db.summaries

st.title("News Summarizer")

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

st.write("Latest summarized news articles")

# Fetch and display summaries
summaries = summary_collection.find().sort("publishedAt", -1).limit(10)
for summary in summaries:
    with st.expander(f"{summary['source']} - {summary['publishedAt']}"):
        st.write(summary["summary"])
        st.markdown(f"[Read more]({summary['url']})")