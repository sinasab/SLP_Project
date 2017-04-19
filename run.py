from lyric_data import getSplitLyricData, reducedData
from lyric_features import getFeaturesBoW, getLyricsFromData
from lyric_labels import getLabels
from perceptron import trainAndEvaluatePerceptron
from naive_bayes import naive_bayes
#from neural_net import run_nn

if __name__ == '__main__':
    # Switch percentage of dataset to use depending on your system
    data = getSplitLyricData(percent=1)
    # data = reducedData()
    # represent the labels and features appropriately
    labels = getLabels(data, 'genre') # {le, train, test, validation}
    features = getFeaturesBoW(data) # {cv, train, test, validation}

    naive_bayes(features["train"], features["test"], labels)
    perceptron_res = trainAndEvaluatePerceptron(features, labels)
    # run_nn(features["train"],features["test"],labels)
