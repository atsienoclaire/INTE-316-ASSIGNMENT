from scipy.interpolate import interp1d
import matplotlib.pyplot as plt
import numpy as np
x_data = [2.00, 4.25, 5.25, 7.81, 9.20, 10.60]
y_data = [7.2, 7.1, 6.0, 5.0, 3.5, 5.0]

spline = interp1d(x_data, y_data, kind='linear')

x_new = np.linspace(2.00, 10.60, num=100)
y_new = spline(x_new)

plt.plot(x_data, y_data, 'o', x_new, y_new, '-')
plt.show()
