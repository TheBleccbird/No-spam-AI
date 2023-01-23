import pandas as pd

from src.model_creation.steps import utils


def data_understanding():
    dataset = pd.read_csv("dataset/dataset_full.csv")

    dataset['subject'] = dataset.subject.astype('string')
    dataset['email_to'] = dataset.email_to.astype('string')
    dataset['email_from'] = dataset.email_from.astype('string')
    dataset['message'] = dataset.message.astype('string')

    print(str(dataset.info()))

    n_duplicati = dataset.duplicated().sum()
    print("\nI duplicati nel dataset di partenza sono " + str(n_duplicati))

    n_mancanti = dataset.isnull().sum()
    print("\nI dati mancanti nel dataset di partenza sono: \n" + str(n_mancanti))

    balanced_count = dataset["label"].value_counts()
    print("\nIl bilanciamento del dataset di partenza è: \n" + str(balanced_count) + "\n")

    utils.create_data_plot(dataset, "Bilanciamento dei dati")

    return dataset
