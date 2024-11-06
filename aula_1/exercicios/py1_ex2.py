# Calculadora de Média de Notas

# Função para calcular a média de uma lista de notas
def calcular_media(notas):
    """
    Calcula a média aritmética de uma lista de notas.
    
    Parâmetros:
    notas (lista de float): Lista contendo as notas dos alunos.
    
    Retorna:
    float: Média das notas.
    """
    soma = sum(notas)  # Soma todas as notas
    quantidade = len(notas)  # Obtém a quantidade total de notas
    media = soma / quantidade  # Calcula a média aritmética
    return media

# Exemplo de uso
if __name__ == "__main__":
    # Lista de notas dos alunos
    notas_alunos = [7.5, 8.0, 9.2, 6.5, 8.7]
    
    # Calcula a média das notas
    media_notas = calcular_media(notas_alunos)
    
    # Exibe o resultado
    print("A média das notas é:", media_notas)
