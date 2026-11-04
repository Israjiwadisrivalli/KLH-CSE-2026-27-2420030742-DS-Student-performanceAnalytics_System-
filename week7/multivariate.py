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


# ---------------- HEATMAP ----------------

plt.figure(figsize=(8, 6))

sns.heatmap(
    df.iloc[:, :4].corr(),
    annot=True,
    cmap="coolwarm"
)

plt.title("Heatmap of Feature Correlations")
plt.show()


# ---------------- BUBBLE CHART ----------------

plt.figure(figsize=(6, 4))

plt.scatter(
    df['sepal length (cm)'],
    df['sepal width (cm)'],
    s=df['petal length (cm)'] * 20,
    alpha=0.5,
    c=df['species']
)

plt.xlabel("Sepal Length (cm)")
plt.ylabel("Sepal Width (cm)")
plt.title("Bubble Chart: Sepal vs Petal (Size = Petal Length)")

plt.show()