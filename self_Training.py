import requests
from bs4 import BeautifulSoup

url = "https://doorayqa.dooray.com/mail/systems/inbox"

res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

with open("dooray.html", "w", encoding="utf8") as f:
    f.write(res.text)