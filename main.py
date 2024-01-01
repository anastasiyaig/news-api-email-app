import requests

api_key = 'ee89c4486b5446dcb8f32294f5721f45'

url = \
    ('https://newsapi.org/v2/everything?q=tesla&from=2023-12-01&sortBy=publishedAt&apiKey'
     '=ee89c4486b5446dcb8f32294f5721f45')

# Do a request
request = requests.get(url)

# Get a dictionary of data
content = request.json()

# Access the article titles and descriptions
for article in content['articles']:
    print(article['title'])
    print(article['description'])

