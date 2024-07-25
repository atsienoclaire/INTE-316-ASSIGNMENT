import numpy as np

from sklearn.linear_model import LinearRegression

x_data = np.array([[1], [2], [3], [4]])
y_data = np.array([2.5, 3.6, 7.1, 8.0])

model = LinearRegression().fit(x_data, y_data)
print(model.coef_, model.intercept_)
