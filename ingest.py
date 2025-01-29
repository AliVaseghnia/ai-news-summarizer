import os
import requests
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

# Connect to MongoDB
client = MongoClient(os.getenv("MONGO_URI"))
db = client.news_db
collection = db.raw_articles

def fetch_news(query="technology"):
    url = "https://newsapi.org/v2/everything"
    params = {
        "q": query,
        "apiKey": os.getenv("NEWSAPI_KEY"),
        "sortBy": "publishedAt",
        "pageSize": 10  # Adjust based on API limits
    }
    response = requests.get(url, params=params)
    articles = response.json().get("articles", [])
    
    # Insert new articles only
    for article in articles:
        if not collection.find_one({"url": article["url"]}):
            collection.insert_one(article)
    print(f"Inserted {len(articles)} new articles.")

if __name__ == "__main__":
    fetch_news()