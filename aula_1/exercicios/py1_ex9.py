# Programa para organizar uma lista de números em ordem crescente

# Função para ordenar uma lista de números de forma crescente
def ordenar_lista(lista):
    # Utilizamos a função sorted() do Python, que retorna uma nova lista com os elementos ordenados
    return sorted(lista)

# Exemplo de uso
if __name__ == "__main__":
    # Solicita ao usuário para inserir uma lista de números separados por vírgula
    numeros_entrada = input("Digite os números separados por vírgula: ")
    
    # Converte a entrada do usuário em uma lista de inteiros
    lista_numeros = [int(numero.strip()) for numero in numeros_entrada.split(",")]
    
    # Ordena a lista
    lista_ordenada = ordenar_lista(lista_numeros)
    
    # Exibe a lista ordenada
    print("Lista em ordem crescente:", lista_ordenada)

# Explicação:
# 1. A função ordenar_lista(lista) usa a função sorted() para ordenar a lista de números.
# 2. Solicitamos ao usuário para inserir os números separados por vírgula.
# 3. Transformamos essa entrada em uma lista de inteiros utilizando list comprehension.
# 4. Chamamos a função para ordenar a lista e exibimos o resultado.

# Exemplo:
# Entrada do usuário: 5, 3, 8, 1, 2
# Saída: Lista em ordem crescente: [1, 2, 3, 5, 8]