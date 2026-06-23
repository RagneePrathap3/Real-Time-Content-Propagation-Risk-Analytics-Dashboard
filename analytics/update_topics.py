import psycopg2
from analytics.topic_classifier import classify_topic

conn = psycopg2.connect(
    host="localhost",
    database="community_risk",
    user="postgres",
    password="Ragnee@postgre33",
    port="5432"
)

cursor = conn.cursor()

cursor.execute("""
SELECT id, title
FROM news_articles
""")

articles = cursor.fetchall()

for article_id, title in articles:

    topic = classify_topic(title)

    cursor.execute(
        """
        UPDATE news_articles
        SET topic = %s
        WHERE id = %s
        """,
        (topic, article_id)
    )

conn.commit()

cursor.close()
conn.close()

print("Topics updated successfully!")