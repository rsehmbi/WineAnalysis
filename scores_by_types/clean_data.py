import numpy as np
import pandas as pd




def get_counts_by_points(data):
	points = data.apply(lambda x: x.value_counts(), axis=0)
	return points