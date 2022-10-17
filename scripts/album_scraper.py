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
    genre = soup.find("th", string="Genre").next_sibling.text
    length = soup.find("th", string="Length").next_sibling.text
    label = soup.find("th", string="Label").next_sibling.text
    released = soup.find("th", string="Released").next_sibling.text
    released = re.sub('\s?\((.*?)\)', '', released)
    tracklist = soup.find_all("table", class_="tracklist")
    tracks = []

    for track in tracklist:
        tracks.extend(re.findall(r'\".*?\"', track.text))

    print(f"{album}, {artist}")
    print("Genres: ", re.sub('\s?\[(.*?)\]', '', genre).strip().split("\n"))
    print("Release date: ", parser.parse(released))
    print("Length: ", length)
    print("Label: ", label.strip().split("\n"))
    print(summary)
    print(tracks)


def run():
    artist = input("Artist name: ")
    album = input("Album name: ")
    url = input("Album Wiki URL: ")
    scrape(artist, album, url)
