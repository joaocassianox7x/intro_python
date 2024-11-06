# Função para trocar os valores de "a" e "b"
def trocar_valores(a, b):
    # Usamos uma variável temporária para armazenar o valor de "a" e fazer a troca
    temp = a
    a = b
    b = temp
    return a, b

# Exemplo de uso
if __name__ == "__main__":
    # Atribui valores iniciais a "a" e "b"
    a = 10
    b = 20
    
    # Exibe os valores antes da troca
    print(f"Antes da troca: a = {a}, b = {b}")
    
    # Troca os valores usando a função
    a, b = trocar_valores(a, b)
    
    # Exibe os valores após a troca
    print(f"Após a troca: a = {a}, b = {b}")

# Explicação:
# 1. A função trocar_valores(a, b) recebe os valores de "a" e "b".
# 2. Utilizamos uma variável temporária "temp" para armazenar o valor de "a".
# 3. Atribuímos o valor de "b" para "a" e, depois, o valor de "temp" para "b".
# 4. Retornamos os novos valores de "a" e "b".
# 5. No exemplo de uso, verificamos os valores antes e após a troca.

# Exemplo:
# Antes da troca: a = 10, b = 20
# Após a troca: a = 20, b = 10
