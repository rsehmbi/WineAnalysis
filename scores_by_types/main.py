import numpy as np
import pandas as pd
import get_data
import clean_data as clean
import visualize_data as vis



def main():
	# Get data from .csv
	data = get_data.get_data()
	# Count the number of points for each point
	points = clean.get_counts_by_points(data)
	vis.get_hist(points, data.min().min(), data.max().max())


if __name__ == '__main__':
	main()