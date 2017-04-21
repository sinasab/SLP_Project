from lyric_data import getSplitLyricData
from lyric_features import getBoW1, getBoW2
from lyric_labels import getLabels
from perceptron import perceptron
from multilayer_perceptron import mlperceptron
from naive_bayes import naive_bayes
from svm import run_svm
# from neural_net import run_nn
# from w2vec import getW2vec

if __name__ == '__main__':
    # Switch percentage of dataset to use depending on your system
    data = getSplitLyricData(percent=.5)
    # represent the labels and features appropriately
    labels = getLabels(data, 'genre') # {le, train, test, validation}
    # labels = getLabels(data, "year")
    features = getBoW1(data) # {cv, train, test, validation}
    # features = getBoW2(data)
    # features = getW2vec(data)

    ptron = perceptron(features, labels)
    # svm = run_svm(features, labels)
    # nb = naive_bayes(features, labels)
    # mlp = mlperceptron(features, labels)
