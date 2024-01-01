import requests
import send_email

api_key = 'ee89c4486b5446dcb8f32294f5721f45'

url = \
    ('https://newsapi.org/v2/everything?'
     'q=tesla&'
     'from=2023-12-01&'
     'sortBy=publishedAt'
     '&apiKey=ee89c4486b5446dcb8f32294f5721f45&'
     'language=en')

# Do a request
request = requests.get(url)

# Get a dictionary of data
content = request.json()

body = ''
# Access the article titles and descriptions
for article in content['articles'][:20]:
    if article['title'] and article['description'] and article['url']:
        body = "Subject: Today's news" + "\n" + body + article['title'] + "\n" + article['description'] + "\n" + article['url'] + 2*"\n"

composed_email = str(body).encode("utf-8")
send_email.send_email(composed_email)
