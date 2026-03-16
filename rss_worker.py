
from backend.utils.rss_importer import import_rss

feeds = [
"https://rss.nytimes.com/services/xml/rss/nyt/Technology.xml",
"https://feeds.bbci.co.uk/news/technology/rss.xml"
]

def collect():

    articles = []

    for feed in feeds:
        articles += import_rss(feed)

    return articles
