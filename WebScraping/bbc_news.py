import requests
from bs4 import BeautifulSoup

url = "https://www.bbc.com/news"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

headlines = soup.find_all("h3", class_="gs-c-promo-heading__title")
for headline in headlines:
    print(headline.text)