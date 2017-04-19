from sklearn import svm
from sklearn.metrics import accuracy_score

def run_svm(train,test,labels):
    clf = svm.SVC()
    clf.fit(train, labels["train"])
    pred = clf.predict(test)
    print accuracy_score(labels["test"],pred)
