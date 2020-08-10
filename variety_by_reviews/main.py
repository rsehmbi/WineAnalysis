import numpy as np
import pandas as pd
import data_cleaning as clean
import data_classification as clf


def main():
    data = pd.read_csv('./data/1442_8172_compressed_winemag-data-130k-v2.csv.zip')
    data = clean.clean_description(data)
    clf.classify_data(data)


if __name__ == '__main__':
    main()