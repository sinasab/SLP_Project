from lyric_data import getSplitLyricData, reducedData
from lyric_features import getFeaturesBoW
from lyric_labels import getLabels
from perceptron import trainAndEvaluatePerceptron
from naive_bayes import naiveBayes

if __name__ == '__main__':
    # Switch percentage of dataset to use depending on your system
    data = getSplitLyricData(percent=0.3)
    # data = reducedData()
    # represent the labels and features appropriately
    labels = getLabels(data, 'genre') # {le, train, test, validation}
    features = getFeaturesBoW(data) # {cv, train, test, validation}
    # perceptron_res = trainAndEvaluatePerceptron(features, labels)

    print naiveBayes(features["train"], features["test"], labels)
