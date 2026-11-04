import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("tips.csv")

sns.countplot(x="sex", hue="day", data=df, palette="Set1")

plt.show()