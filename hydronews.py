from newsapi import NewsApiClient
import datetime as dt
import pandas as pd

newsapi = NewsApiClient(api_key='XXXXXXXX')

data = newsapi.get_everything(q='Water',
                                     
                                      language='en',
                                      sort_by='relevancy',
                                      )



articles = data['articles']
print(articles[0])
