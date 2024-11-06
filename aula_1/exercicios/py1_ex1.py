# Função para calcular o menor elemento de uma lista
def menor_elemento(lista):
    # Verifica se a lista não está vazia
    if not lista:
        return None  # Retorna None se a lista estiver vazia

    # Inicializa o menor elemento como o primeiro da lista
    menor = lista[0]

    # Percorre cada elemento da lista
    for elemento in lista:
        # Compara o elemento atual com o menor encontrado até agora
        if elemento < menor:
            menor = elemento  # Atualiza o menor elemento

    # Retorna o menor elemento encontrado
    return menor

# Exemplo de uso da função
numeros = [10, 5, 3, 8, 2, 7]
resultado = menor_elemento(numeros)
print("O menor elemento da lista é:", resultado)
