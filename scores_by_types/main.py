import numpy as np
import pandas as pd
from get_data import get_data
import clean_data




def main():
	data = get_data()
	points = clean_data.get_counts_by_points(data)



if __name__ == '__main__':
	main()