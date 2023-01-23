import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB


def data_modeling():
    # leggo il dataset target
    finalDataset = pd.read_csv("dataset/dataset_final.csv")

    # per evitare problemi derivati dal non essere un tipo stringa li converto in stringa
    finalDataset['subject-email_from-message'] = finalDataset['subject-email_from-message'].astype('string')

    finalDatasetArray = []
    finalDatasetArrayLabel = []

    # TfidfVectorizer accetta solo una lista di stringhe in input quindi le creo
    for i in range(len(finalDataset)):
        words = finalDataset.iloc[i]["subject-email_from-message"]
        result = finalDataset.iloc[i]["label"]
        finalDatasetArray.append(words)
        finalDatasetArrayLabel.append(result)

    X_train, X_test, y_train, y_test = train_test_split(finalDatasetArray, finalDatasetArrayLabel, test_size=0.20,
                                                        random_state=0)

    feature_extractor = TfidfVectorizer(stop_words='english', lowercase=True)
    X_train_features = feature_extractor.fit_transform(X_train)
    print(feature_extractor.vocabulary_)
    X_test_features = feature_extractor.transform(X_test)

    # per il momento scelgo il Naive Bayes
    classifier = MultinomialNB()
    classifier.fit(X_train_features, y_train)

    # ritorno il classificatore, i dati di test convertiti ed il vectorizer per usi nelle fasi successive
    return classifier, X_test_features, y_test, feature_extractor
