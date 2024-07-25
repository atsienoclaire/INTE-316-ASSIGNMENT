def lagrange_interpolation(x_points, y_points):
    def L(k, x):
        term = 1
        for i in range(len(x_points)):
            if i != k:
                term *= (x - x_points[i]) / (x_points[k] - x_points[i])
        return term
    
    def P(x):
        result = 0
        for i in range(len(x_points)):
            result += y_points[i] * L(i, x)
        return result
    
    return P

# Given data points
x_points = [1, 2, 3, 4]
y_points = [1, 4, 9, 16]

# Compute the Lagrange polynomial
P = lagrange_interpolation(x_points, y_points)

# Example usage
x = 2.5
y = P(x)
y
