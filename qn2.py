import pandas as pd
df = pd.read_csv("Q2-Dataset.csv")
emptyRows = df[df.isnull().any(axis=1)]
print(emptyRows)
df.fillna("Not specified", inplace=True)
print(df)
