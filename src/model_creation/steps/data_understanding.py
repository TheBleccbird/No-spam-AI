import pandas as pd
from matplotlib import pyplot as plt


def data_understanding():
    dataset = pd.read_csv("dataset/dataset_full.csv")

    dataset['subject'] = dataset.subject.astype('string')
    dataset['email_to'] = dataset.subject.astype('string')
    dataset['email_from'] = dataset.subject.astype('string')
    dataset['email_message'] = dataset.subject.astype('string')

    print(str(dataset.info()))

    n_duplicati = dataset.duplicated().sum()
    print("\nI duplicati nel dataset di partenza sono " + str(n_duplicati))

    n_mancanti = dataset.isnull().sum()
    print("\nI dati mancanti nel dataset di partenza sono: \n" + str(n_mancanti))

    balanced_count = dataset["label"].value_counts()
    print("\nIl bilanciamento del dataset di partenza è: \n" + str(balanced_count) + "\n")

    return dataset
