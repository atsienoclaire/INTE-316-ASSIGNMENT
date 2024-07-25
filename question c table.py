import numpy as np

# Given data points
x_values = np.array([2.00, 4.25, 5.25, 7.81, 9.20, 10.60])
y_values = np.array([7.2, 7.1, 6.0, 5.0, 3.5, 5.0])

# Linear interpolation function
def linear_spline(x, x_values, y_values):
    for i in range(len(x_values) - 1):
        if x_values[i] <= x <= x_values[i+1]:
            x1, x2 = x_values[i], x_values[i+1]
            y1, y2 = y_values[i], y_values[i+1]
            y = y1 + ((x - x1) * (y2 - y1)) / (x2 - x1)
            return y
    return None

# Find y at x = 4.0
x_target = 4.0
y_target = linear_spline(x_target, x_values, y_values)
y_target
