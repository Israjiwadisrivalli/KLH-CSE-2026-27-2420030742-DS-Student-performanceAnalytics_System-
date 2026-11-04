import pandas as pd

data = {
    "Name": ["Mahesh Babu", "Samantha", "Allu Arjun", "Rashmika", "Prabhas"],
    "Sub DS": [85, 92, 76, 88, 70],
    "TOC": [78, 89, 81, 93, 74],
    "CD": [90, 85, 79, 87, 82],
    "QC": [82, 94, 75, 90, 78],
    "ASE": [88, 91, 84, 89, 76]
}

df = pd.DataFrame(data)

print(df.to_string(index=False))