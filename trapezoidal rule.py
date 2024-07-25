import numpy as np

def trapezoidal_rule(f, a, b, n):
    """
    Approximate the integral of f(x) from a to b using the trapezoidal rule with n trapezoids.
    
    Parameters:
    f : function
        The integrand function.
    a : float
        The start point of the integration.
    b : float
        The end point of the integration.
    n : int
        The number of trapezoids.
        
    Returns:
    float
        The approximate value of the integral.
    """
    x = np.linspace(a, b, n+1)  # n+1 points make n trapezoids
    y = f(x)
    
    h = (b - a) / n
    integral = (h / 2) * (y[0] + 2 * np.sum(y[1:-1]) + y[-1])
    
    return integral

# Example usage
if __name__ == "__main__":
    # Define the function to be integrated
    def f(x):
        return x**2  # Example: integrate x^2 from 0 to 1

    # Integration limits
    a = 0
    b = 1

    # Number of trapezoids
    n = 1000

    # Compute the integral
    result = trapezoidal_rule(f, a, b, n)

    print(f"The approximate integral of f(x) from {a} to {b} is {result}")
