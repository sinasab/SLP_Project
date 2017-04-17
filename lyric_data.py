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
import random

TRAIN_PERCENTAGE = 0.7
VALIDATION_PERCENTAGE = 0.15
TEST_PERCENTAGE = 0.15

def getSplitLyricData(percent=0.3):
    ''' Return a tuple of (train, validation, test) data lists '''
    allData = [dp for dp in getAllLyricData() if dp["lyrics"] != '']
    # shuffle it, seeding the rng for consistency while developing
    random.seed(0)
    random.shuffle(allData)
    # find indices of where to slice allData
    total_len = int(len(allData) * percent)
    train_cutoff = int(TRAIN_PERCENTAGE * total_len)
    val_cutoff = int(VALIDATION_PERCENTAGE * total_len) + train_cutoff
    # create slices of the data
    train = allData[:train_cutoff]
    validation = allData[train_cutoff:val_cutoff]
    test = allData[val_cutoff:total_len]
    return { "train": train, "validation": validation, "test": test }

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

def reducedData():
    data = [dp for dp in getFewLyricData() if dp["lyrics"]]
    random.seed(0)
    random.shuffle(data)
    total_len = len(data)
    train_cutoff = int(TRAIN_PERCENTAGE * total_len)
    val_cutoff = int(VALIDATION_PERCENTAGE * total_len) + train_cutoff
    train = data[:train_cutoff]
    validation = data[train_cutoff:val_cutoff]
    test = data[val_cutoff:]
    return { "train": train, "validation": validation, "test": test }