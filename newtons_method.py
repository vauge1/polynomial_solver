# newtons_method.py

# Define the polynomial function p(x) = x^3 - 7x - 40
def p(x):
    return x**3 - 7*x - 40

# Define the derivative of the polynomial function p'(x) = 3x^2 - 7
def p_prime(x):
    return 3*x**2 - 7

# Implement Newton's Method
def newtons_method(func, func_prime, initial_guess, tolerance=1e-4, max_iterations=100):
    x = initial_guess
    for _ in range(max_iterations):
        next_x = x - func(x) / func_prime(x)
        if abs(next_x - x) < tolerance:
            return next_x
        x = next_x
    return x
