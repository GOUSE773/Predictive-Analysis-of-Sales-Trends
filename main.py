

import matplotlib.pyplot as plt

# Sample sales data
dates = ['2020-01-01', '2020-02-01', '2020-03-01', '2020-04-01', '2020-05-01', '2020-06-01']
sales = [100, 120, 130, 145, 160, 170]


def calculate_linear_regression(x, y):
    n = len(x)
    sum_x = sum(x)
    sum_y = sum(y)
    sum_xy = sum(x[i] * y[i] for i in range(n))
    sum_x_squared = sum(x[i] ** 2 for i in range(n))

    slope = (n * sum_xy - sum_x * sum_y) / (n * sum_x_squared - sum_x ** 2)
    intercept = (sum_y - slope * sum_x) / n

    return slope, intercept

# Convert date strings to numerical values
date_values = [i for i in range(len(dates))]


slope, intercept = calculate_linear_regression(date_values, sales)


future_months = 3
predicted_sales = [slope * (i + len(dates)) + intercept for i in range(future_months)]

# Combine actual and predicted sales data
all_dates = dates + [f'2020-{i + len(dates) + 1:02d}-01' for i in range(future_months)]
all_sales = sales + predicted_sales

# Createing line graph using Matplotlib
plt.figure(figsize=(10, 6))
plt.plot(all_dates, all_sales, marker='o', linestyle='-')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.title('Sales Trend Over Time')
plt.grid(True)

#Rotate x-axis
plt.xticks(rotation=45)

#finally displaying the graph
plt.tight_layout()
plt.show()

dates = ['2020-01-01', '2020-02-01', '2020-03-01', '2020-04-01', '2020-05-01', '2020-06-01']
sales = [100, 120, 130, 145, 160, 170]
