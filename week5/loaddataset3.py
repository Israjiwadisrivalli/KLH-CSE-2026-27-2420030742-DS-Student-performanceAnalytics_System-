import seaborn as sns
data=sns.load_dataset("tips")
sns.countplot(y='sex',hue='smoker',data=data)
