from newsapi import NewsApiClient
import os

def get_news(keyword='technology'):
    newsapi = NewsApiClient(api_key=os.getenv('NEWS_API_KEY'))
    try:
        news = newsapi.get_everything(q=keyword, language='en', sort_by='relevancy', page_size=20)  # Limit to 20 articles
        articles = []
        for article in news['articles']:
            articles.append({
                'title': article['title'],
                'source': article['source']['name'],
                'published_at': article['publishedAt'],
                'url': article['url']
            })
        return articles
    except Exception as e:
        print(f"Error fetching news: {e}")
        return []