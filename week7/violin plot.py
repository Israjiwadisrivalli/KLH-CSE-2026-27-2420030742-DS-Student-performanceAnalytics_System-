import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

# Load Iris dataset
iris = load_iris()

# Create DataFrame
df = pd.DataFrame(iris.data, columns=iris.feature_names)

# Add species column
df['species'] = iris.target

# Violin plot
plt.figure(figsize=(6, 4))

sns.violinplot(x='species', y='sepal length (cm)', data=df)

plt.title('Violin Plot of Iris Species')
plt.xlabel('Species')
plt.ylabel('Sepal Length (cm)')

plt.show()