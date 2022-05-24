from hudba.models import Review, Album
import requests
from bs4 import BeautifulSoup
import csv


def review_scrape():
    global album
    global artist

    print("Album: ")
    album = input()

    print("Artist: ")
    artist = input()

    try:
        Album.objects.get(name=album, artist__name=artist)
    except:
        print("Album not found in database.")
        return False

    page = requests.Session()
    page.headers["User-Agent"] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36'
    scrape = page.get(f"https://www.metacritic.com/music/{album.replace(' ', '-').lower()}/{artist.replace(' ', '-').lower()}")
    soup = BeautifulSoup(scrape.content, "html.parser")

    if scrape.status_code != 200:
        print("Reviews not available.")
        return False

    review_save(soup)


def review_save(soup):
    reviewers = []
    ratings = []
    reviews = []

    for reviewer in soup.find_all('div', attrs={'class': 'source'}):
        reviewers.append(reviewer.get_text().strip())

    for i in soup.find_all('ol', attrs={'class': 'reviews critic_reviews'}):
        rating_descendants = i.descendants
        for rating in rating_descendants:
            if rating.name == 'div' and rating.get('class', '') == ['review_grade']:
                ratings.append(rating.text.strip())

    for i in soup.find_all('ol', attrs={'class': 'reviews critic_reviews'}):
        review_descendants = i.descendants
        for review in review_descendants:
            if review.name == 'div' and review.get('class', '') == ['review_body']:
                reviews.append(review.text.strip())

    with open('../review.csv', 'w', newline='', encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["reviewer", "rating", "text"])
        for a, b, c in zip(reviewers, ratings, reviews):
            print(writer.writerow([a, b, c]))


review_scrape()


def run():
    with open("../review.csv", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader)  # Advance past the header

        for row in reader:
            _, created = Review.objects.get_or_create(
                reviewer=row[0],
                rating=row[1],
                text=row[2],
                reviewed_id=Album.objects.get(name=album, artist__name=artist).pk
            )

# https://towardsdatascience.com/use-python-scripts-to-insert-csv-data-into-django-databases-72eee7c6a433
