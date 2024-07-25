from scipy.integrate import quad

def integrand(x):
    return x**2 - x - 2

result, _ = quad(integrand, 1, 3)
print(result)
