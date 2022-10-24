from bs4 import BeautifulSoup
from dateutil import parser
import requests
import re
import wikipedia


def scrape(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')

    album = soup.find("h1", id="firstHeading").text
    print(album)
    artist = soup.find("div", class_="contributor").text
    print(artist)
    genres = soup.find("th", string="Genre").next_sibling
    length = soup.find("th", string="Length").next_sibling.text
    label = soup.find("th", string="Label").next_sibling.text
    released = soup.find("th", string="Released").next_sibling.text
    released = re.sub(r'\s?\((.*?)\)', '', released)
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
        print(f"There are {len(tracklist)} tracklists in total:")
        for track in tracklist:
            print(track.find("caption").text)
        choice = list(map(int, input("Enter multiple values: ").split()))
        for x in choice:
            tracks_list.extend(re.findall(r'\".*?\"', tracklist[x-1].text))

    genres_list = [i for i in genres_list if i]

    print(f"{album}, {artist}")
    print("Genres: ", genres_list)
    print("Release date: ", parser.parse(released))
    print("Length: ", length)
    print("Label: ", label.strip().split("\n"))
    print(summary)
    print(tracks_list)


def run():
    url = input("Album Wiki URL: ")
    scrape(url)
