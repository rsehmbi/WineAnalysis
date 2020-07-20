import pandas as pd


def get_data():
	data = pd.read_csv('data_wine/top-five-wine-scores.csv', index_col=0)
	return data

