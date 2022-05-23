import requests
from bs4 import BeautifulSoup

page = requests.Session()
page.headers["User-Agent"] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36'
scrape = page.get("https://www.metacritic.com/music/immutable/meshuggah")
print(scrape)

soup = BeautifulSoup(scrape.content, "html.parser")

for reviewer in soup.find_all('div', attrs={'class': 'source'}):
    print(reviewer.get_text().strip())

for foo in soup.find_all('ol', attrs={'class': 'reviews critic_reviews'}):
    foo_descendants = foo.descendants
    for d in foo_descendants:
        if d.name == 'div' and d.get('class', '') == ['review_grade']:
            print(d.text.strip())

for foo in soup.find_all('ol', attrs={'class': 'reviews critic_reviews'}):
    foo_descendants = foo.descendants
    for d in foo_descendants:
        if d.name == 'div' and d.get('class', '') == ['review_body']:
            print(d.text.strip())
