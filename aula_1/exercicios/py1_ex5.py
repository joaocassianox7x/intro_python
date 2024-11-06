# Função para calcular o fatorial de um número
# O fatorial de um número n é o produto de todos os inteiros positivos menores ou iguais a n
# Exemplo: fatorial de 5 (5!) = 5 * 4 * 3 * 2 * 1 = 120

def fatorial(n):
    # Verificamos se o número é menor que zero, pois o fatorial não está definido para números negativos
    if n < 0:
        return "Fatorial não está definido para números negativos."
    
    # O fatorial de 0 e 1 é 1
    if n == 0 or n == 1:
        return 1
    
    # Calcula o fatorial através de um loop
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    
    return resultado

# Exemplo de uso
numero = 5
print(f"O fatorial de {numero} é: {fatorial(numero)}")

# Saída esperada:
# O fatorial de 5 é: 120
