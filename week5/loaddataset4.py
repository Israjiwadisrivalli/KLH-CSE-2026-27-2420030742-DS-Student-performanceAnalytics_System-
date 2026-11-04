import seaborn as sns
data=sns.load_dataset("tips")
sns.boxplot(data['size'])