import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("tips")

sns.displot(df["total_bill"], kde=False, color="red", bins=20)

plt.show()