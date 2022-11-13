from datetime import timedelta
from bs4 import BeautifulSoup
from hudba.models import Album, Track, Genre, Label, Artist
from dateutil import parser
from PIL import Image
import re
import csv
import ast
import click
import requests
import wikipedia


def timeconvert(time):
    sec = sum(x * int(t) for x, t in zip([60, 1], time.split(":")))
    length = timedelta(seconds=sec)
    return length


def scrape(url, image_url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')

    album = soup.find("h1", id="firstHeading").text
    artist = soup.find("div", class_="contributor").text
    genres = soup.find("th", string="Genre").next_sibling
    length = soup.find("th", string="Length").next_sibling.text
    label = soup.find("th", string="Label").next_sibling.text.strip().split("\n")
    released = soup.find("th", string="Released").next_sibling.text
    released = parser.parse(re.sub(r'\s?\((.*?)\)', '', released))
    summary = wikipedia.summary(f"{album} (album)")
    tracklist = soup.find_all("table", class_="tracklist")
    tracks_list = []
    genres_list = []

    if not genres.find_all("li"):
        for genre in genres.find_all("a"):
            genres_list.append(re.sub(r'\s?\[(.*?)]', '', genre.text))
    else:
        for genre in genres.find_all("li"):
            genres_list.append(re.sub(r'\s?\[(.*?)]', '', genre.text))

    if len(tracklist) == 1:
        for track in tracklist:
            tracks_list.extend(re.findall(r'\".*?\"', track.text))
    else:
        print(f"\nThere are {len(tracklist)} tracklists in total:")
        for index, track in enumerate(tracklist, start=1):
            try:
                tracklist_name = track.find("caption").text
            except AttributeError:
                tracklist_name = "--- (couldn't get a name)"
            print(index, tracklist_name)
        choice = list(map(int, input("Enter which playlists to add: ").split()))
        for x in choice:
            for row in tracklist[x-1].tbody.find_all('tr'):
                columns = row.find("th", {"id": lambda t: t and t.startswith('track')})
                if columns is not None:
                    tracks_list.extend(re.findall(r'^(".*?")', columns.next_sibling.text))

    genres_list = [i for i in genres_list if i]

    print("\nScraper has found following data:")
    print(f"{artist}, {album}")
    print("Genres: ", genres_list)
    print("Release date: ", released)
    print("Length: ", length)
    print("Label: ", label)
    print("Summary: ", summary)
    for number, track in enumerate(tracks_list, start=1):
        print(f"{number}. {track}")

    img = Image.open(requests.get(image_url, stream=True).raw)
    img.save(f'media/albums/{album}.png')

    with open('temp.csv', 'w', newline='', encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["album", "artist", "summary", "date", "length", "image_path", "genres", "tracklist"])
        writer.writerow([artist, album, summary, released.strftime("%Y-%m-%d"), timeconvert(length),
                         str(f"albums/{album}.png"), genres_list, tracks_list])

    if click.confirm('\nData have been saved. Do you want to push them to db?', default=True):
        with open("temp.csv", "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            next(reader)  # Advance past the header

            for row in reader:
                objx, created = Album.objects.get_or_create(
                    artist_id=Artist.objects.get(name=row[0]).pk,
                    name=row[1],
                    about=row[2],
                    release_date=row[3],
                    length=row[4],
                    cover=row[5],
                    label_id=Label.objects.get_or_create(name=label[0])[0].pk,
                )

                for genre in ast.literal_eval(row[6]):
                    objy, created = Genre.objects.get_or_create(
                        name=genre.replace('\'', '', 2)
                    )
                    objx.genre.add(objy.__class__.objects.get(name=genre.replace('\'', '', 2)).pk)

                for number, track in enumerate(ast.literal_eval(row[7]), start=1):
                    objz, created = Track.objects.get_or_create(
                        name=re.sub('["\']', '', track),
                        album_id=Album.objects.get(name=row[1]).pk,
                        number=number
                    )

                print("Done.")
    else:
        print("Closing program...")


def run():
    url = input("Album Wiki URL: ")
    image_url = input("Album Cover URL: ")
    scrape(url, image_url)
