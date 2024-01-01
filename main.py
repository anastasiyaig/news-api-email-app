from datetime import datetime, date, timedelta

import requests

import send_email

api_key = 'ee89c4486b5446dcb8f32294f5721f45'
topic = "tesla"
language = "en"
from_date = str(date.today() - timedelta(days=1))
sort_by = 'publishedAt'

url = \
    ('https://newsapi.org/v2/everything?'
     f'q={topic}&'
     f'from={from_date}&'
     f'sortBy={sort_by}&'
     f'apiKey={api_key}&'
     f'language={language}')

# Do a request
request = requests.get(url)

# Get a dictionary of data
content = request.json()

body = ''
# Access the article titles and descriptions
for article in content['articles'][:20]:
    if article['title'] and article['description'] and article['url']:
        body = "Subject: Today's news" + "\n" + body + article['title'] + "\n" + article['description'] + "\n" + \
               article['url'] + 2 * "\n"

composed_email = str(body).encode("utf-8")
send_email.send_email(composed_email)
