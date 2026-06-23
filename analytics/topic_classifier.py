TOPICS = {
    "Politics": [
        "trump", "government", "election",
        "congress", "senate", "starmer",
        "israel", "iran"
    ],

    "Technology": [
        "google", "apple", "microsoft",
        "android", "pixel", "technology"
    ],

    "Health": [
        "health", "cancer",
        "hospital", "medical"
    ],

    "Finance": [
        "investor", "stock",
        "market", "finance",
        "fed", "economy"
    ],

    "Entertainment": [
        "celebrity", "music",
        "actor", "movie",
        "dua", "lipa"
    ]
}

def classify_topic(title):

    if not title:
        return "Other"

    title = title.lower()

    for topic, keywords in TOPICS.items():

        for keyword in keywords:

            if keyword in title:
                return topic

    return "Other"