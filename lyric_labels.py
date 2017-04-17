from sklearn.preprocessing.label import LabelEncoder

def getLabels(splitData, key):
    le = LabelEncoder()

    # gets training labels and puts them in the full data object
    training_labels = le.fit_transform([data[key] for data in splitData["train"]])
    for i in range(len(splitData["train"])):
        splitData["train"][i]["labels"] = training_labels[i]

    # cleans up data to make sure classification works properly
    removeUnseenLabelData(splitData, le, key)

    # gets testing labels and puts them in the full data object
    testing_labels = le.transform([data[key] for data in splitData["test"]])
    for i in range(len(splitData["test"])):
        splitData["test"][i]["labels"] = testing_labels[i]

    # gets validation labels and puts them in the full data object
    validation_labels = le.transform([data[key] for data in splitData["validation"]])
    for i in range(len(splitData["validation"])):
        splitData["validation"][i]["labels"] = validation_labels[i]

    return {
        "train": training_labels,
        "test": testing_labels,
        "validation": validation_labels
    }

def removeUnseenLabelData(splitData, le, key):
    class_set = set(le.classes_)

    # clean up testing data
    new_test_data = []    
    for lyric in splitData["test"]:
        if lyric[key] in class_set:
            new_test_data.append(lyric)
    splitData["test"] = new_test_data

    # clean up validation data
    new_validation_data = []    
    for lyric in splitData["validation"]:
        if lyric[key] in class_set:
            new_validation_data.append(lyric)
    splitData["validation"] = new_validation_data