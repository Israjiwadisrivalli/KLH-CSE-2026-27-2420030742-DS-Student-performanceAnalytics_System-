import seaborn as sns
import pandas as pd
df=pd.read_csv('/content/temporal.csv')
df=sns.boxplot(df['data science'])