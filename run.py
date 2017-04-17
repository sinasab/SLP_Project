from lyric_data import *
from sklearn.feature_extraction.text import CountVectorizer

if __name__ == '__main__':
    count_vect = CountVectorizer()
    data = getSplitupLyricData()
    train = data['train']
    validate = data['validation']
    test = data['test']
    train_lyrics = getLyricsFromData(train)
    valid_lyrics = getLyricsFromData(validate)
    test_lyrics = getLyricsFromData(test)

    train_counts = count_vect.fit_transform(train_lyrics)
    validate_counts = count_vect.transform(valid_lyrics)
    test_counts = count_vect.transform(test_lyrics)
    print train_counts.shape
    print validate_counts.shape
    print test_counts.shape
