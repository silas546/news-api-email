import requests

api_key = "43c6edecbcfa4159a10f99aaedaf054f"
url = "https://newsapi.org/v2/top-headlines?"\
       "country=us&category=business&apiKey="\
       "43c6edecbcfa4159a10f99aaedaf054f"

# Make the api request
request = requests.get(url)

# Convert data to dictionary
content = request.json()

# Access title/description
for article in content["articles"]:
    print(article["title"])
    print(article["description"])

