from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

def naive_bayes(train, test, labels):
    clf = MultinomialNB().fit(train, labels["train"])
    predicted = clf.predict(test)
    print accuracy_score(labels["test"],predicted)