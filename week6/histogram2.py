import seaborn as sns
import matplotlib.pyplot as plt

data = sns.load_dataset("iris")

sns.violinplot(x='species', y='petal_length', data=data)

plt.title('Violin plot')

plt.show()

