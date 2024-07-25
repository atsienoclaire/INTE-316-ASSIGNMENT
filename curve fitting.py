import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# Example data
x_data = np.array([1, 2, 3, 4])
y_data = np.array([2.5, 3.6, 7.1, 8.0])

# Define the model function
def model_func(x, a, b):
    return a * x + b

# Fit the curve
params, _ = curve_fit(model_func, x_data, y_data)
a, b = params

# Plot the data and the fitted curve
plt.scatter(x_data, y_data, label='Data')
plt.plot(x_data, model_func(x_data, a, b), label='Fitted curve', color='red')
plt.legend()
plt.show()
