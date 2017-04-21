from sklearn.linear_model import Perceptron
import numpy as np

def perceptron(data, labels):
    p = Perceptron(
        n_iter=200,
        #verbose=True,
        shuffle=True,
        random_state=0
    )
    p.fit(data["train"], labels["train"])
    print p.score(data["test"], labels["test"])
    return p
