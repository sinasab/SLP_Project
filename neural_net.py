import tensorflow.contrib.learn as skflow
import tensorflow as tf
import numpy as np
from sklearn import datasets, metrics
from scipy.sparse import csr_matrix


def run_nn(train, test, labels):
    feature_columns = [tf.contrib.layers.real_valued_column("", dimension=4)]
    classifier = skflow.DNNClassifier(feature_columns=feature_columns,hidden_units=[10, 20, 10], n_classes=12)
    train_input = get_train_inputs(train,labels)
    classifier.fit(input_fn=train_input,steps=2000)
    score = metrics.accuracy_score(labels["test"], classifier.predict(test))
    print score

# Define the train inputs
def get_train_inputs(train, labels):
    x = tf.sparse_tensor_to_dense(convert_csr_to_tensor(train))
    y = tf.constant(labels["train"])
    return x, y


def convert_csr_to_tensor(X):
    coo = X.tocoo()
    indices = np.mat([coo.row, coo.col]).transpose()
    return tf.SparseTensor(indices, coo.data, coo.shape)
