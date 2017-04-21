"""
Runs a multilayer perceptron on the lyric data
"""
from sklearn.neural_network import MLPClassifier

def mlPerceptron(x, y):
    mlp = MLPClassifier(
        # hidden_layer_sizes=(5,3,2),
        random_state=0,
        shuffle=True,
        # verbose=True,
        max_iter=50
    )
    mlp.fit(x["train"], y["train"])
    print mlp.score(x["test"], y["test"])
    return mlp
