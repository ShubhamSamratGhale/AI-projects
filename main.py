```python
import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv(NEWS_API_KEY)


def get_top_headlines(country=us, category=technology):
    url = fhttps://newsapi.org/v2/top-headlines?country={country}&amp;category={category}&amp;apiKey={API_KEY}
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        articles = data.get(articles, [])
        if not articles:
            print(No news found.)
            return
        print(fTop {category.capitalize()} News in {country.upper()}:)
        for i, article in enumerate(articles[:5], 1):
            print(f\n{i}. {article['title']})
            print(f   Source: {article['source']['name']})
            print(f   URL: {article['url']})
    else:
        print(Error:, response.status_code, response.json())


get_top_headlines(us, technology)
```
