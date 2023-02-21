#Your API key is: 1a8fc8c198474d50b44399f138dcaae2
import requests


class NewsFeed:
    '''Representing multiple news articles and links
    '''
    base_url = "https://newsapi.org/v2/top-headlines?country=us&"
    api_key = "1a8fc8c198474d50b44399f138dcaae2"

    def __init__(self, interest, from_date, to_date, language='en'):
        self.interest = interest
        self.from_date = from_date
        self.to_date = to_date
        self.language = language

    def get(self):
        url = self._build_url()

        articles = self._get_articles(url)

        email_body = ''
        for article in articles:
            email_body = email_body +"\n"+ article['title'] + "\n" + article['url'] + "\n\n"

        return email_body

    def _get_articles(self, url):
        response = requests.get(url)
        content = response.json()
        articles = content['articles']
        return articles


    def _build_url(self):
        url = f"{self.base_url}" \
            f"qInTitle={self.interest}&"\
            f"from={self.from_date}&"\
            f"to={self.to_date}&"\
            "language=en"\
            f"apiKey={self.api_key}"
        return url

if __name__ == "__main__":
    news_feed = NewsFeed(interest='nasa')
    print(news_feed.get())
    print(NewsFeed.todays_date)
