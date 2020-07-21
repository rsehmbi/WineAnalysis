import numpy as np
import matplotlib.pyplot as plt



def get_hist(points, range_min, range_max):
	scores = np.arange(range_min, range_max+1)
	width=0.2
	plt.figure(figsize=(15,10))
	plt.bar(scores-(width*2), points['Bordeaux-style Red Blend'],align='center', width=width, color='r', edgecolor='white')
	plt.bar(scores-width, points['Cabernet Sauvignon'], align='center', width=width, color='b', edgecolor='white')
	plt.bar(scores, points['Chardonnay'], align='center', width=width, color='g', edgecolor='white')
	plt.bar(scores+width, points['Pinot Noir'], align='center', width=width, color='m', edgecolor='white')
	plt.bar(scores+(width*2), points['Red Blend'], align='center', width=width, color='y', edgecolor='white')
	plt.xticks(scores)
	plt.legend(['Bordeaux-style Red Blend','Cabernet Sauvignon','Chardonnay','Pinot Noir','Red Blend'])
	plt.xlabel('Scores')
	plt.ylabel('Count')
	# plt.show()
	plt.savefig('./outputs/wine_scores_by_types.png')
