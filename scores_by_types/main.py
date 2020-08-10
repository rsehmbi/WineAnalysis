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
	# vis.plot_bar_indi(points, data.min().min(), data.max().max())
	# vis.plot_bar_counts(points, data.min().min(), data.max().max())
	# vis.plot_violin(data)
	init_normal_p, init_lev_p = anal.get_normal_levene_tests(data)
	init_variances = anal.get_variance(data)
	# out.initial_test_to_csv(init_normal_p, init_lev_p, init_variances)
	anova_p = anal.get_anova(data)
	print("anova p-value = {}".format(anova_p))


if __name__ == '__main__':
	main()