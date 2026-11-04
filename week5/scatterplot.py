import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv("temporal.csv")
plt.scatter(df['deep learning'],df['machine learning'],color = 'red',marker='^')
plt.title('Scatter Plot')
plt.xlabel("Deep Learning")
plt.ylabel("Machine Learning")
plt.show()
plt.frid()
plt.show()