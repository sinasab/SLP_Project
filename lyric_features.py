import re
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer

def getFeaturesBoW(splitData):
    # bag of words featurizer

    vectorizer = TfidfVectorizer(strip_accents="ascii", tokenizer=tokenizer, ngram_range=(2, 2))
    #vectorizer = CountVectorizer(strip_accents="ascii", tokenizer=tokenizer, ngram_range=(2, 2))
    # fit and transform the train data lyrics
    train_lyrics = getLyricsFromData(splitData["train"])
    train_features = vectorizer.fit_transform(train_lyrics)
    for i in range(len(splitData["train"])):
        splitData["train"][i]["features"] = train_features[i]
    # transform test and validation data groups
    test_lyrics = getLyricsFromData(splitData["test"])
    test_features = vectorizer.transform(test_lyrics)
    for i in range(len(splitData["test"])):
        splitData["test"][i]["features"] = test_features[i]
    validation_lyrics = getLyricsFromData(splitData["validation"])
    validation_features = vectorizer.transform(validation_lyrics)
    for i in range(len(splitData["validation"])):
        splitData["validation"][i]["features"] = validation_features[i]
    splitData["cv"] = vectorizer
    return {
        "cv": vectorizer,
        "train": train_features,
        "test": test_features,
        "validation": validation_features
    }

def tokenizer(doc):
    delims = "[ \n\[\]:]" # regex of our delimiters; \n, sp, and some puncts.
    return [token for token in re.split(delims, doc)
        if token is not ''
    ]

def getLyricsFromData(data):
    return [song['lyrics'] for song in data]
