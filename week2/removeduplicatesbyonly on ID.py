#Removing duplicates
import pandas as pd
#sample dataset wth duplicates
df = pd.DataFrame({
    'Name':['Alice','Bob','Bob','Charlie','David','David','David'],
    'Age': [25, 30, np.nan, 40, 35],
})
print("Original Data:\n",df)
#remove exact duplicates
df_exact = df.drop_duplicates(subset=['ID'])
print("\nAfter Subset-Based Removal(ID):\n",df_Subset)