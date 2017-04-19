from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

def naive_bayes(train_counts, test_counts, labels):
    tfidf_transformer = TfidfTransformer()
    train_tfidf = tfidf_transformer.fit_transform(train_counts)
    clf = MultinomialNB().fit(train_tfidf, labels["train"])
    test_tfidf = tfidf_transformer.transform(test_counts)
    predicted = clf.predict(test_tfidf)
    print accuracy_score(labels["test"],predicted)
