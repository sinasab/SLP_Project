from lyric_data import getSplitupLyricData, reducedData
from lyric_features import setFeaturesBoW

if __name__ == '__main__':
    # Switch between reduced and full data set depending on your system
    #data = getSplitupLyricData()
    data = reducedData()
    
    res = setFeaturesBoW(data) # {cv, train, test, validation}
    cv = res["cv"] # the CountVectorizer
    train_counts = res["train"]
    validate_counts = res["validation"]
    test_counts = res["test"]

    print train_counts.shape
    print validate_counts.shape
    print test_counts.shape
