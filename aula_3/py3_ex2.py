import numpy as np

# Criação da matriz aleatória
N, M = 4, 5
matrix = np.random.randint(1, 10, size=(N, M))

# Soma utilizando broadcasting
broadcast_sum = np.sum(matrix)

# Soma utilizando loops
loop_sum = 0
for i in range(N):
    for j in range(M):
        loop_sum += matrix[i][j]

print(f"Matriz:\n{matrix}")
print(f"Soma (Broadcasting): {broadcast_sum}")
print(f"Soma (Loops): {loop_sum}")
