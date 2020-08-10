import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns



def plot_bar_counts(points, range_min, range_max):
	sns.set()
	scores = np.arange(range_min, range_max+1)
	width = 0.2
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
	plt.show()

def plot_violin(points):
	sns.set()
	ax = sns.violinplot(data=points)
	plt.title('Kernel Density Estimate with Box Plot of Wine Types Scores', fontsize=19)
	plt.xlabel('Wine Types', fontsize=15)
	plt.ylabel('Score', fontsize=15)
	plt.show()

def plot_bar_indi(points, range_min, range_max):
	sns.set()
	scores = np.arange(range_min, range_max+1)
	fig, axes = plt.subplots(nrows=3, ncols=2)
	axes[0, 0].bar(scores, points['Bordeaux-style Red Blend'], color='r')
	axes[0, 0].set(title='Bordeaux-style Red Blend')
	axes[0, 1].bar(scores, points['Cabernet Sauvignon'], color='b')
	axes[0, 1].set(title='Cabernet Sauvignon')
	axes[1, 0].bar(scores, points['Chardonnay'], color='g')
	axes[1, 0].set(title='Chardonnay')
	axes[1, 1].bar(scores, points['Pinot Noir'], color='m')
	axes[1, 1].set(title='Pinot Noir')
	axes[2, 0].bar(scores, points['Red Blend'], color='y')
	axes[2, 0].set(title='Red Blend')
	fig.delaxes(axes[2, 1])
	for ax in axes.flat:
		ax.set(xlabel='Score', ylabel='Count')
	plt.show()