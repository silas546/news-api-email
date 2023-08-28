import requests
from mailer import send_email

api_key = "43c6edecbcfa4159a10f99aaedaf054f"
url = "https://newsapi.org/v2/top-headlines?"\
       "country=us&category=business&apiKey="\
       "43c6edecbcfa4159a10f99aaedaf054f"

# Make the api request
request = requests.get(url)

# Convert data to dictionary
content = request.json()


# Construct an email body via our data
def output_headlines():
    output_msg = ""
    for article in content["articles"][:11]:
        output_msg += str(article["title"]) + "\n"
        output_msg += str(article["description"]) + "\n"
        output_msg += article["url"] + 2*"\n"
    return output_msg


raw_message = output_headlines()


message = f"""\
Subject: Business news headlines

{raw_message}\n

"""
message = message.encode('utf8')
print(message)


send_email(message=message)
