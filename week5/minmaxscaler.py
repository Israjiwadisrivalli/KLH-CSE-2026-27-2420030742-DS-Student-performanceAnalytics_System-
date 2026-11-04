import pandas as pd
from sklearn.preprocessing import MinMaxScaler

data = pd.DataFrame({
    'A': [10, 20, 30, 40, 50],
    'B': [5, 15, 25, 35, 45]
})

print("Original Data:")
print(data)

scaler = MinMaxScaler()

normalized_data = scaler.fit_transform(data)

normalized_data = pd.DataFrame(
    normalized_data,
    columns=data.columns
)

print("\nNormalized Data:")
print(normalized_data)