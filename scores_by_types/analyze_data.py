from scipy import stats
import pandas as pd


def get_normality(data):
	p = stats.normaltest(data, nan_policy='omit').pvalue
	return p

def get_variance(smp_1, smp_2, smp_3, smp_4, smp_5):
	sigma = stats.levene(smp_1, smp_2, smp_3, smp_4, smp_5).pvalue
	return sigma

def get_analysis(data):
	p_values = data.apply(get_normality, axis=0)
	sigma = get_variance(data.iloc[:,0], data.iloc[:,1], data.iloc[:,2], data.iloc[:,3], data.iloc[:,4])
	return p_values, sigma