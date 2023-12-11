import pandas as pd
data = pd.read_csv('ds_salaries.csv')

print(data.head())
print("\n")

print(data.shape)
print("\n")

print(data.job_title)
print("\n")
print(data['salary_in_usd'])
print("\n")
print(data.iloc[3:11, :])
print("\n")
print(data.salary_in_usd.describe())
