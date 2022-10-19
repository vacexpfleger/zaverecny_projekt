from bs4 import BeautifulSoup
from dateutil import parser
import requests
import re
import wikipedia


def scrape(artist, album, url):
    URL = url
    page = requests.get(URL)

    soup = BeautifulSoup(page.text, 'html.parser')

    summary = wikipedia.summary(album)
    genres = soup.find("th", string="Genre").next_sibling
    length = soup.find("th", string="Length").next_sibling.text
    label = soup.find("th", string="Label").next_sibling.text
    released = soup.find("th", string="Released").next_sibling.text
    released = re.sub('\s?\((.*?)\)', '', released)
    tracklist = soup.find_all("table", class_="tracklist")
    tracks_list = []
    genres_list = []

    for genre in genres.find_all("li"):
        genres_list.append(re.sub('\s?\[(.*?)]', '', genre.text))

    for track in tracklist:
        tracks_list.extend(re.findall(r'\".*?\"', track.text))

    print(f"{album}, {artist}")
    print("Genres: ", genres_list)
    print("Release date: ", parser.parse(released))
    print("Length: ", length)
    print("Label: ", label.strip().split("\n"))
    print(summary)
    print(tracks_list)


def run():
    artist = input("Artist name: ")
    album = input("Album name: ")
    url = input("Album Wiki URL: ")
    scrape(artist, album, url)



