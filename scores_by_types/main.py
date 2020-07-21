import numpy as np
import pandas as pd
import get_data
import clean_data as clean
import visualize_data as vis
import analyze_data as anal
import output_data as out



def main():
	data = get_data.get_data()
	points = clean.get_counts_by_points(data)
	# vis.get_hist(points, data.min().min(), data.max().max())
	init_pvalues, init_sigma = anal.get_analysis(points)
	out.initial_test_to_csv(init_pvalues, init_sigma)


if __name__ == '__main__':
	main()