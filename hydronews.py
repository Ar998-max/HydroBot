from newsapi import NewsApiClient
import datetime as dt
import pandas as pd

newsapi = NewsApiClient(api_key='603a030f4cc64883b2e9340cdebbbc36')

data = newsapi.get_everything(q='Water',
                                     
                                      language='en',
                                      sort_by='relevancy',
                                      )



articles = data['articles']
print(articles[0])