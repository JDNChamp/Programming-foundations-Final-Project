import matplotlib.pyplot as plt
from part_1 import data
#generating a box plot
plt.boxplot(data.salary_in_usd)
plt.show()
#generating a bar graph
x = data.job_title
y = data.salary_in_usd
plt.bar(x,y, color='magenta')
plt.xlabel('job')
plt.ylabel('salary')
plt.show()
#generating a histogram
plt.hist(y, bins=30)
plt.xlabel("Salary")
plt.ylabel('Frequency')
plt.show()