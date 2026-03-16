
import feedparser

def import_rss(url):

    feed = feedparser.parse(url)

    articles = []

    for entry in feed.entries[:10]:

        articles.append({
            "title": entry.title,
            "content": entry.summary,
            "source": entry.link
        })

    return articles
