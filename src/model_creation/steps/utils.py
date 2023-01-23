from matplotlib import pyplot as plt


def create_data_plot(dataset, title):
    count = dataset["label"].value_counts()

    data = [count[1], count[0]]
    labels = ['spam', 'non-spam']
    colors = ["red", "green"]

    plt.pie(data, labels=labels, colors=colors, autopct='%.0f%%')

    plt.title(title)
    plt.show()
