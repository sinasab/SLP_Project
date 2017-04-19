from sklearn.linear_model import Perceptron
import numpy as np

def trainAndEvaluatePerceptron(data, labels):
    p = Perceptron(n_iter=50)
    p.fit(data["train"], labels["train"])
    print p.score(data["test"], labels["test"])
