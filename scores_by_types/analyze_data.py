from scipy import stats
import numpy as np
import pandas as pd


def get_normality(data):
	p = stats.normaltest(data, nan_policy='omit').pvalue
	return p

def get_levene(smp_1, smp_2, smp_3, smp_4, smp_5):
	lev_p = stats.levene(smp_1, smp_2, smp_3, smp_4, smp_5).pvalue
	return lev_p

def get_normal_levene_tests(data):
	p_values = data.apply(get_normality, axis=0)
	lev_p = get_levene(data.iloc[:,0], data.iloc[:,1], data.iloc[:,2], data.iloc[:,3], data.iloc[:,4])
	return p_values, lev_p

def get_variance(data):
	variances = data.apply(lambda x: np.var(x), axis=0)
	return variances