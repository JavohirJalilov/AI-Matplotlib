import matplotlib.pyplot as plt
import csv

data = open('mnist_test.csv')
def get_data(data):
    reader = csv.reader(data)
    dataset = []
    for rows in reader:
        k = 1
        number_data = []
        row = []
        for i in rows:
            row.append(int(i))
            if k == 28:
                number_data.append(row)
                k = 0
                row = []
            k += 1
        dataset.append(number_data)

    return dataset

def data_imshow(data_number):
    plt.imshow(data_number,cmap='gray')
    plt.show()


dataset = get_data(data)
data_imshow(dataset[2002])