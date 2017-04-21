from sklearn import svm
from sklearn.metrics import accuracy_score

def run_svm(features,labels):
    train = features["train"]
    test = features["test"]
    clf = svm.SVC()
    clf.fit(train, labels["train"])
    pred = clf.predict(test)
    print accuracy_score(labels["test"],pred)
    return clf
