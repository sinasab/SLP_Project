from lyric_data import getSplitLyricData, reducedData
from lyric_features import getFeaturesBoW
from lyric_labels import getLabels
from perceptron import trainAndEvaluatePerceptron

if __name__ == '__main__':
    # Switch percentage of dataset to use depending on your system
    data = getSplitLyricData(percent=0.3)
    # data = reducedData()
    # represent the labels and features appropriately
    labels_res = getLabels(data, 'genre') # {le, train, test, validation}
    features_res = getFeaturesBoW(data) # {cv, train, test, validation}
    # perceptron_res = trainAndEvaluatePerceptron(res, labels)
