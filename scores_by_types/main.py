import numpy as np
import pandas as pd
from get_data import get_data
import clean_data
import visualize_data as visual



def main():
	# Get data from .csv
	data = get_data()
	# Count the number of points for each point
	points = clean_data.get_counts_by_points(data)
	visual.get_hist(points, data.min().min(), data.max().max())




if __name__ == '__main__':
	main()