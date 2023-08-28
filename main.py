import requests

api_key = "43c6edecbcfa4159a10f99aaedaf054f"
url = "https://newsapi.org/v2/top-headlines?"\
       "country=us&category=business&apiKey="\
       "43c6edecbcfa4159a10f99aaedaf054f"

request = requests.get(url)
content = request.text
print(content)
