import numpy as np
import tensorflow as tf


def read_data(training_frac=0.7):
    """Returns two tuples of data+labels from a training file. The first tuple is training data, the second is test."""
    all_data = np.loadtxt('training.txt', dtype='int8', delimiter=',')
    np.random.shuffle(all_data)
    # Split data into training and test data sets
    training_data, test_data = np.split(all_data, [int(len(all_data * training_frac))])
    # Data is stored in a format where the first 18 numbers represent the board state and the last 9 numbers represent
    # which moves are optimal (labels). Note that the labels are not one-hot (multiple moves may be optimal).
    for s in (training_data, test_data):
        data, labels = np.split(s, [18], axis=1)
        yield data, labels


def main():
    np.random.seed(0)
    print(read_data())


if __name__ == '__main__':
    main()
