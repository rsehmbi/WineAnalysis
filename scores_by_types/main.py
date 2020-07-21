import numpy as np
import pandas as pd
import get_data
import clean_data as clean
import visualize_data as vis
import analyze_data as anal
import output_data as out
import transform_data as tf



def main():
	data = get_data.get_data()
	points = clean.get_counts_by_points(data)
	# vis.get_bar(points, data.min().min(), data.max().max())
	init_normal_p, init_lev_p = anal.get_normal_levene_tests(points)
	init_variances = anal.get_variance(points)
	out.initial_test_to_csv(init_normal_p, init_lev_p, init_variances)

	# points_tf = tf.get_sqrt(points)
	# normal_p_tf, sigma_tf = anal.get_normal_levene_tests(points_tf)
	# print(normal_p_tf, sigma_tf)
	# vis.get_bar(points_tf, 80, 100)


if __name__ == '__main__':
	main()