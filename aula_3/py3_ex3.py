import numpy as np
import matplotlib.pyplot as plt

# Definição do polinômio: f(x) = ax^3 + bx^2 + cx + d
a, b, c, d = 1, -3, 2, 5
def f(x):
    return a * x**3 + b * x**2 + c * x + d

# Derivada do polinômio
def df(x):
    return 3 * a * x**2 + 2 * b * x + c

# Geração de valores
x_vals = np.linspace(-3, 3, 100)
y_vals = f(x_vals)
y_prime_vals = df(x_vals)

# Plotagem
plt.figure(figsize=(10, 6))
plt.plot(x_vals, y_vals, label="f(x) - Polinômio")
plt.plot(x_vals, y_prime_vals, label="f'(x) - Derivada", linestyle="--")
plt.title("Polinômio e sua Derivada")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid()
plt.show()
