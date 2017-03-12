import numpy as np
import tensorflow as tf


def read_data():
    """Returns the data and labels from a training file."""
    all_data = np.loadtxt('training.txt', dtype='int8', delimiter=',')
    # Data is stored in a format where the first 18 numbers represent the board state and the last 9 numbers represent
    # which moves are optimal (labels). Note that the labels are not one-hot (multiple moves may be optimal).
    data, labels = np.split(all_data, [18], axis=1)
    return data, labels



def main():
    print(read_data())


if __name__ == '__main__':
    main()
