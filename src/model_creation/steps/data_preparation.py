import pandas as pd
import steps.data_preprocessing as pr
import steps.utils as utils
import sklearn


def data_preparation(dataset):
    cleaned_dataset = data_cleaning(dataset)
    balanced_dataset = data_balancing(cleaned_dataset)
    final_dataset_creation(balanced_dataset)


def data_cleaning(dataset):
    # la colonna email_to non è utile per identificare un'email spam quindi viene eliminata
    dataset = dataset.drop(dataset.columns[[2]], axis=1)

    # elimino i duplicati
    dataset = dataset.drop_duplicates()

    # elimino le righe che hanno valore null o simili
    dataset = dataset.dropna()

    balanced_count = dataset["label"].value_counts()
    print("\nIl bilanciamento del dataset dopo la rimozione duplicati e valori null è: \n" + str(balanced_count) + "\n")
    utils.create_data_plot(dataset, "Bilanciamento dataset dopo la pulizia di duplicati e valori null")

    # viene eseguita la pipeline di pulizia dati
    pr.clean_up_pipeline(dataset)

    # dopo queste fasi potrebbero uscire altre righe vuote, le elimino
    dataset = dataset.dropna()
    balanced_count = dataset["label"].value_counts()
    print("\nIl bilanciamento del dataset dopo le fasi di pulizia è: \n" + str(balanced_count) + "\n")
    utils.create_data_plot(dataset, "Bilanciamento dataset dopo le fasi di pulizia")

    return dataset


def final_dataset_creation(dataset):
    # creo il dataset target
    finalDataset = pd.DataFrame(columns=["label", "subject-email_from-message"])

    print("Inizio il salvataggio del nuovo csv")

    # inserisco tutti i nuovi dati nel file finale
    for i in range(len(dataset)):
        print("Generazione della riga: " + str(i) + "/" + str(len(dataset)))
        label = dataset.iloc[i]["label"]
        subject = dataset.iloc[i]["subject"]
        email_from = dataset.iloc[i]["email_from"]
        message = dataset.iloc[i]["message"]

        row = [label, subject + " " + email_from + " " + message]
        finalDataset.loc[len(finalDataset)] = row

    # converto in csv il DataFrame
    finalDataset.to_csv("dataset/dataset_final.csv", index=False)
