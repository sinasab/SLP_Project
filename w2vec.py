import re
import gensim
import numpy as np
from lyric_features import tokenizer, getLyricsFromData

# you have to download this and put it in data folder:
# https://drive.google.com/file/d/0B7XkCwpI5KDYNlNUTTlSS21pQmM/edit
model = gensim.models.KeyedVectors.load_word2vec_format('./data/GoogleNews-vectors-negative300.bin', binary=True)

def getW2vec(splitData):
    # Load Google's pre-trained Word2Vec model.
    #vectorizer = CountVectorizer(strip_accents="ascii", tokenizer=tokenizer, ngram_range=(2, 2))
    features = {}
    for datagroup in ["train", "test", "validation"]:
        group_lyrics = getLyricsFromData(splitData[datagroup])
        features[datagroup] = []
        for i in range(len(group_lyrics)):
            songfeatures = np.zeros(300)
            tokens_in_song = 0
            for token in tokenizer(group_lyrics[i]):
                if token in model:
                    songfeatures += model[token]
                    tokens_in_song += 1
            if tokens_in_song > 0 and True:
                songfeatures /= tokens_in_song
            splitData[datagroup][i]["features"] = songfeatures
            features[datagroup].append(songfeatures)
    splitData["w2vec"] = model
    return {
        "w2vec": model,
        "train": features["train"],
        "test": features["test"],
        "validation": features["validation"]
    }
