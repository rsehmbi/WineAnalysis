import numpy as np
import pandas as pd
import clean_data as clean


def main():
    # data = pd.read_csv('./data/winemag-data-130k-v2.csv')
    data = pd.read_csv('./data/1442_8172_compressed_winemag-data-130k-v2.csv.zip')
    clean.clean_description(data)

if __name__ == '__main__':
    main()