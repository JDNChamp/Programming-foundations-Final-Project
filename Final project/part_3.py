import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

data = pd.read_csv('ds_salaries.csv')
x = data.experience_level
x = pd.get_dummies(data=x, drop_first=True)
y = data.salary_in_usd

x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=1)

re = LinearRegression()
re.fit(x_train, y_train)
y_pre = re.predict(x_test)
print(y_pre)
print(re.score(x_test, y_test))
