import numpy as np

# Função ReLU
def relu(x):
    return np.maximum(0, x)

# Derivada da ReLU
def relu_derivative(x):
    return np.where(x > 0, 1, 0)

# Backpropagation simples
def backpropagation(inputs, weights, target, learning_rate):
    # Forward pass
    z = np.dot(inputs, weights)
    a = relu(z)
    
    # Loss (MSE)
    loss = np.mean((a - target)**2)
    
    # Backward pass
    grad_loss = 2 * (a - target) / len(target)  # Gradiente da Loss
    grad_relu = grad_loss * relu_derivative(z)  # Gradiente ReLU
    grad_weights = np.dot(inputs.T, grad_relu)  # Gradiente dos pesos
    
    # Atualização dos pesos
    weights -= learning_rate * grad_weights
    return weights, loss

# Exemplo de uso
np.random.seed(42)
inputs = np.random.rand(4, 3)  # 4 exemplos, 3 características
weights = np.random.rand(3, 1)  # 3 características, 1 saída
target = np.array([[1], [0], [1], [0]])  # Saída esperada
learning_rate = 0.1

# Treinamento
epochs = 10
for epoch in range(epochs):
    weights, loss = backpropagation(inputs, weights, target, learning_rate)
    print(f"Época {epoch + 1}: Loss = {loss:.4f}")
