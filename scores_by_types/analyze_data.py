from scipy import stats
import numpy as np
import pandas as pd
from scipy import stats


def get_normality(data):
	p = stats.normaltest(data, nan_policy='omit').pvalue
	return p

def get_levene(smp_1, smp_2, smp_3, smp_4, smp_5):
	lev_p = stats.levene(smp_1, smp_2, smp_3, smp_4, smp_5).pvalue
	return lev_p

def get_normal_levene_tests(data):
	p_values = data.apply(get_normality, axis=0)
	lev_p = get_levene(data.iloc[:,0].dropna(), data.iloc[:,1].dropna(), data.iloc[:,2].dropna(), data.iloc[:,3].dropna(), data.iloc[:,4].dropna())
	return p_values, lev_p

def get_variance(data):
	# variances = data.apply(lambda x: np.var(x))
	variances = data.var(axis=0)
	return variances

def get_anova(data):
	anova_p = stats.f_oneway(data['Bordeaux-style Red Blend'].dropna(),data['Cabernet Sauvignon'].dropna(),data['Chardonnay'].dropna(),
							data['Pinot Noir'].dropna(),data['Red Blend'].dropna()).pvalue
	return anova_p
