import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

# Load Iris dataset
iris = load_iris()

# Create DataFrame
df = pd.DataFrame(iris.data, columns=iris.feature_names)

# Add species
df['species'] = iris.target


# ---------------- SCATTER PLOT ----------------

plt.figure(figsize=(6, 4))

sns.scatterplot(
    x=df['sepal length (cm)'],
    y=df['sepal width (cm)'],
    hue=df['species']
)

plt.title("Scatterplot: Sepal Length vs Sepal Width")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Sepal Width (cm)")
plt.show()


# ---------------- LINE CHART ----------------

plt.figure(figsize=(6, 4))

plt.plot(df['sepal length (cm)'])

plt.title("Line Chart of Sepal Length")
plt.xlabel("Sample Index")
plt.ylabel("Sepal Length (cm)")
plt.show()


# ---------------- BAR CHART ----------------

plt.figure(figsize=(6, 4))

sns.barplot(
    x=df['species'],
    y=df['sepal length (cm)']
)

plt.title("Bar Chart: Mean Sepal Length by Species")
plt.xlabel("Species")
plt.ylabel("Sepal Length (cm)")
plt.show()
