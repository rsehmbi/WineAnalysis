import pandas as pd



# Put variables together for one .csv file.
def get_output_format(normal_p, lev, variances):
	pvalues_df = pd.DataFrame({'pvalues': normal_p})
	variances_df = pd.DataFrame({'variance': variances})
	lev_df = pd.DataFrame({'variance': [lev]}, index=['levene test'])
	var_lev_df = variances_df.append(lev_df)
	p_v_l = pd.concat([pvalues_df, var_lev_df], axis=1)
	return p_v_l

# Output to .csv the initial normal test and levene test.
def initial_test_to_csv(normal_p, lev, variances):
	p_v_l = get_output_format(normal_p, lev, variances)
	print(p_v_l)
	p_v_l.to_csv('./outputs/initial_normal_levene_tests.csv')