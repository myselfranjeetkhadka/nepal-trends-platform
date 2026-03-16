
from workers.rss_worker import collect
from backend.utils.summarizer import summarize

def publish():

    news = collect()

    for article in news:

        summary = summarize(article["content"])

        print("Publishing:", article["title"])

if __name__ == "__main__":
    publish()
