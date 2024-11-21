import numpy as np
import matplotlib.pyplot as plt

# Definição do polinômio: f(x) = ax^2 + bx + c
a, b, c = 1, -3, 2
def f(x):
    return a * x**2 + b * x + c

# Derivada do polinômio
def df(x):
    return 2 * a * x + b

# Gradiente descendente
def gradient_descent(start_x, learning_rate, iterations):
    x = start_x
    history = [x]
    for _ in range(iterations):
        grad = df(x)
        x = x - learning_rate * grad
        history.append(x)
    return x, history

# Parâmetros do gradiente descendente
start_x = 5
learning_rate = 0.1
iterations = 50

# Execução
min_x, history = gradient_descent(start_x, learning_rate, iterations)

# Visualização
x_vals = np.linspace(-1, 5, 100)
y_vals = f(x_vals)

plt.figure(figsize=(10, 6))
plt.plot(x_vals, y_vals, label="f(x)")
plt.scatter(history, [f(x) for x in history], color="red", label="Iterações do Gradiente")
plt.title("Gradiente Descendente em um Polinômio de Segundo Grau")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid()
plt.show()
