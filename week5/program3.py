import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("temporal.csv")

plt.bar(df['deep learning'], df['machine learning'], color='red')

plt.xlabel('Deep Learning')
plt.ylabel('Machine Learning')
plt.title('Bar Plot')

plt.show()