import numpy as np

def newton_divided_difference(x_points, y_points):
    n = len(y_points)
    coef = np.zeros([n, n])
    coef[:, 0] = y_points
    
    for j in range(1, n):
        for i in range(n - j):
            coef[i][j] = (coef[i + 1][j - 1] - coef[i][j - 1]) / (x_points[i + j] - x_points[i])
    
    def P(x):
        result = coef[0, 0]
        for i in range(1, n):
            term = coef[0, i]
            for j in range(i):
                term *= (x - x_points[j])
            result += term
        return result
    
    return P

# Compute the Newton polynomial
P_newton = newton_divided_difference(x_points, y_points)

# Example usage
y_newton = P_newton(x)
y_newton
