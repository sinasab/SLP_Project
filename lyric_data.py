"""
Return either all of or a few of the lyrics tuples as a list of dictionaries.

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

def getAllLyricData():
    # return all of the data
    lyricsData = []
    for datafile in glob.glob("./data/lyrics/lyrics_*.csv"):
        with open(datafile, "r") as f:
            fieldnames = ["index", "song", "year", "artist", "genre", "lyrics"]
            for row in csv.DictReader(f, fieldnames=fieldnames):
                lyricsData.append(row)
    return lyricsData

def getFewLyricData():
    # return a subset of the data
    lyricsData = []
    for datafile in glob.glob("./data/lyrics/lyrics_[0-2].csv"):
        with open(datafile, "r") as f:
            fieldnames = ["index", "song", "year", "artist", "genre", "lyrics"]
            for row in csv.DictReader(f, fieldnames=fieldnames):
                lyricsData.append(row)
    return lyricsData