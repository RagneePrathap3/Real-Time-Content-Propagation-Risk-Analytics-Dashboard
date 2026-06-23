import requests
import pandas as pd
from dotenv import load_dotenv
import os

from database.db import get_connection

load_dotenv()

API_KEY = os.getenv("NEWS_API_KEY")

url = (
    f"https://newsapi.org/v2/top-headlines?"
    f"language=en&"
    f"pageSize=20&"
    f"apiKey={API_KEY}"
)

response = requests.get(url)

data = response.json()

articles = data.get("articles", [])

rows = []

for article in articles:
    rows.append({
        "title": article.get("title"),
        "source": article.get("source", {}).get("name"),
        "published_at": article.get("publishedAt"),
        "author": article.get("author"),
        "url": article.get("url")
    })

df = pd.DataFrame(rows)

print(df.head())

conn = get_connection()

cursor = conn.cursor()

for article in rows:

    cursor.execute(
        """
        INSERT INTO news_articles
        (
            title,
            source,
            author,
            article_url,
            published_at
        )
        VALUES (%s,%s,%s,%s,%s)
        """,
        (
            article["title"],
            article["source"],
            article["author"],
            article["url"],
            article["published_at"]
        )
    )

conn.commit()

cursor.close()
conn.close()

print("Articles inserted successfully!")