import numpy as np

def gradient_descent(f, grad_f, x0, y0, learning_rate, max_iterations):
    x, y = x0, y0
    for _ in range(max_iterations):
        grad_x, grad_y = grad_f(x, y)
        x = x - learning_rate * grad_x
        y = y - learning_rate * grad_y
    return x, y

def function(x, y):
    return x**2 + y**2 - xy + x - y + 1

def gradient(x, y):
    grad_x = 2 * x - y + 1
    grad_y = 2 * y - x - 1
    return grad_x, grad_y

# Initial guess
x0, y0 = 0, 0
# Learning rate
learning_rate = 0.1
# Number of iterations
max_iterations = 1000

# Perform gradient descent
min_x, min_y = gradient_descent(function, gradient, x0, y0, learning_rate, max_iterations)
print(f"Minimum value found at x = {min_x}, y = {min_y}")
