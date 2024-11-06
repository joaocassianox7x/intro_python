# Função para gerar a sequência de Fibonacci até o enésimo termo
def fibonacci(n):
    # Verifica se o número de termos é válido
    if n <= 0:
        print("Por favor, insira um número positivo.")
        return []
    elif n == 1:
        return [0]  # Se o termo for 1, retorna apenas o primeiro termo (0)
    elif n == 2:
        return [0, 1]  # Se o termo for 2, retorna os dois primeiros termos (0, 1)
    
    # Para termos maiores, inicializa a sequência com os dois primeiros números (0, 1)
    sequence = [0, 1]

    # Gera os próximos termos da sequência de Fibonacci
    for i in range(2, n):
        next_term = sequence[-1] + sequence[-2]  # O próximo termo é a soma dos dois anteriores
        sequence.append(next_term)  # Adiciona o novo termo à sequência
    
    return sequence

# Exemplo de uso
n = 10  # Número de termos da sequência desejada
resultado = fibonacci(n)
print(f"Os primeiros {n} termos da sequência de Fibonacci são: {resultado}")
