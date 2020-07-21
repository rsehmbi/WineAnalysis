import pandas as pd



# Output to .csv the initial normal test and levene test.
def initial_test_to_csv(normal_p, sigma):
	pvalues_df = pd.DataFrame({'pvalues': normal_p})
	sigma_df = pd.DataFrame({'variance': [sigma]}, index=['levene'])
	init_p_s = pd.concat([pvalues_df, sigma_df], axis=1)
	print(init_p_s)
	# init_p_s.to_csv('./outputs/initial_normal_levene_tests.csv')