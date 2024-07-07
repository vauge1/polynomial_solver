# plot_polynomial.py

import matplotlib.pyplot as plt
import numpy as np

# Function to plot the polynomial and mark the root
def plot_polynomial(p, root):
    # Define the range of x values for plotting
    x_values = np.linspace(2, 6, 400)  # Generate 400 points between 2 and 6
    y_values = p(x_values)

    # Plot the polynomial function
    plt.figure(figsize=(10, 6))
    plt.plot(x_values, y_values, label='p(x) = x^3 - 7x - 40')
    plt.axhline(0, color='black', linewidth=0.5)  # x-axis
    plt.axvline(0, color='black', linewidth=0.5)  # y-axis
    plt.scatter(root, p(root), color='red', zorder=5)  # Mark the root found by Newton's Method
    plt.title('Graph of p(x) = x^3 - 7x - 40')
    plt.xlabel('x')
    plt.ylabel('p(x)')
    plt.legend()
    plt.grid(True)
    plt.show()
