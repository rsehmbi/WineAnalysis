import numpy as np
import pandas as pd




# Replace NaN with zeros.
def replace_nan(data):
	data = data.fillna(0)
	return data

# Count the number of points for each point
def get_counts_by_points(data):
	points = data.apply(lambda x: x.value_counts(), axis=0)
	points = replace_nan(points)
	return points
