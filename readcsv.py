import pandas as pd

df = pd.read_csv("sample.csv")
print(df.head())


data = {"name": "John Doe", "age": 30, "city": "New York"}
df1 = pd.DataFrame(data)
print(df1)
