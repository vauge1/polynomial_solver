# main.py

from newtons_method import p, p_prime, newtons_method
from plot_polynomial import plot_polynomial
import numpy as np

# Evaluate the polynomial at x = 3 and x = 5
p_3 = p(3)
p_5 = p(5)

# Print the results
print("p(3) =", p_3)
print("p(5) =", p_5)

# Use Newton's Method to approximate a root starting with an initial guess of 4 (since 3 < r < 5)
root = newtons_method(p, p_prime, 4)

# Print the approximated root
print("Approximated root:", round(root, 4))

# Plot the polynomial function and the approximated root
plot_polynomial(p, root)

# Evaluate the polynomial at the approximated root
p_root = p(root)

# Print the result
print("p(root) =", p_root)
