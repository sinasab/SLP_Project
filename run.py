from lyric_data import getSplitLyricData, reducedData
from lyric_features import getFeaturesBoW, getLyricsFromData
from lyric_labels import getLabels
from perceptron import trainAndEvaluatePerceptron
from multilayer_perceptron import trainAndEvaluateMLP
from naive_bayes import naive_bayes
from svm import run_svm
#from neural_net import run_nn

if __name__ == '__main__':
    # Switch percentage of dataset to use depending on your system
    data = getSplitLyricData(percent=.5)
    # data = reducedData()
    # represent the labels and features appropriately
    labels = getLabels(data, 'genre') # {le, train, test, validation}
    features = getFeaturesBoW(data) # {cv, train, test, validation}

    run_svm(features["train"], features["test"], labels)
    naive_bayes(features["train"], features["test"], labels)
    perceptron_res = trainAndEvaluatePerceptron(features, labels)
    # mlp_res = trainAndEvaluateMLP(features, labels)
    # run_nn(features["train"],features["test"],labels)
