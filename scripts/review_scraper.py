import os

import click
from django.db.models import Avg
from hudba.models import Review, Album
import requests
from bs4 import BeautifulSoup
import csv


def select():
    for album in Album.objects.all():
        print(f"{album.name} by {album.artist} ({album.pk})")

    pk = int(input("Select album (enter pk): "))
    url = str(input("Enter Metacritic album link: "))
    scrape(pk, url)


def scrape(choice, url):
    page = requests.Session()
    page.headers["User-Agent"] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36'
    scrape = page.get(url)
    soup = BeautifulSoup(scrape.content, "html.parser")

    if scrape.status_code != 200:
        print("Reviews not available.")
        quit()

    save_to_csv(choice, soup)


def save_to_csv(choice, soup):
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

    with open('temp.csv', 'w', newline='', encoding="utf-8") as output:
        writer = csv.writer(output)
        writer.writerow(["reviewer", "rating", "text"])
        for a, b, c in zip(reviewers, ratings, reviews):
            writer.writerow([a, b, c])

    print(f"There are {len(reviewers)} reviews in total: ")
    for review in reviewers:
        print(review)

    if click.confirm('\nReviews have been saved. Do you want to push them to db?', default=True):
        save_to_db(choice)
        print("Done.")
    else:
        print("Closing program...")
        exit()


def save_to_db(choice):
    album = Album.objects.get(id=choice).name
    artist = Album.objects.get(id=choice).artist

    with open("temp.csv", encoding="utf-8") as inputcsv:
        reader = csv.reader(inputcsv, delimiter=',')
        next(reader)
        for row in reader:
            _, created = Review.objects.get_or_create(
                reviewer=row[0],
                rating=row[1],
                text=row[2],
                reviewed_id=Album.objects.get(name=album, artist__name=artist).pk
            )

    rating_avg = Review.objects.filter(reviewed_id=Album.objects.get(name=album, artist__name=artist).pk).aggregate(Avg("rating"))
    rating_avg = int(round(rating_avg.get("rating__avg"), 0))
    Album.objects.filter(id=Album.objects.get(name=album, artist__name=artist).pk).update(rating=rating_avg)


def run():
    select()

# https://towardsdatascience.com/use-python-scripts-to-insert-csv-data-into-django-databases-72eee7c6a433
