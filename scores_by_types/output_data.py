import pandas as pd




def normality_df(normal_p):
	pvalues_df = pd.DataFrame({'normality': normal_p})
	return pvalues_df

def variance_df(variances):
	variances_df = pd.DataFrame({'variance': variances})
	# lev_df = pd.DataFrame({'variance': [lev]}, index=['levene test'])
	# var_lev_df = variances_df.append(lev_df)
	return variances_df

# Put variables together for one .csv file.
def get_output_df(normal_p, variances):
	pvalues_df = normality_df(normal_p)
	variances_df = variance_df(variances)
	# p_v_l = pd.concat([pvalues_df, var_lev_df], axis=1)
	return pvalues_df, variances_df

# Output to .csv the initial normal test and levene test.
def initial_test_to_csv(normal_p, lev, variances):
	pvalues_df, variances_df = get_output_df(normal_p, variances)
	print('\n{}'.format(pvalues_df))
	print('\n{}'.format(variances_df))
	print("\nlevene test      {}".format(lev))