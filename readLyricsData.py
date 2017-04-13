"""
Reads all of the files from ./data/lyrics/lyrics_*.csv into a list of dictionaries.

You can access the list of dictionaries with the lyricsData variable.

In other files with the same relative path, that's `from readLyricsData import lyricsData`

The dictionaries look like this:
    {
        'index': '20',
        'song': 'beautiful-liar-spanglish-version',
        'year': '2007',
        'artist': 'beyonce-knowles',
        'genre': 'Pop'
        'lyrics': "Ay! Ay!\n(Nobody likes being played)...",
    }
"""
import glob
import csv

lyricsData = []

for datafile in glob.glob("./data/lyrics/lyrics_*.csv"):
    with open(datafile, "r") as f:
        fieldnames = ["index", "song", "year", "artist", "genre", "lyrics"]
        for row in csv.DictReader(f, fieldnames=fieldnames):
            lyricsData.append(row)