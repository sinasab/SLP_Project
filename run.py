from lyric_data import getSplitupLyricData, reducedData
from lyric_features import setFeaturesBoW
from lyric_labels import getLabels

if __name__ == '__main__':
    # Switch between reduced and full data set depending on your system
    #data = getSplitupLyricData()
    data = reducedData()

    # gets desired labels for artist classification while also modifying
    # data to get rid of unseen artists in test and validation sets
    labels = getLabels(data, 'artist')
    
    res = setFeaturesBoW(data) # {cv, train, test, validation}
    cv = res["cv"] # the CountVectorizer
    train_counts = res["train"]
    validate_counts = res["validation"]
    test_counts = res["test"]

    print train_counts.shape
    print validate_counts.shape
    print test_counts.shape
