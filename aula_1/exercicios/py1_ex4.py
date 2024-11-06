# Função para contar o número de vogais em uma string
def contar_vogais(texto):
    # Definir uma string com todas as vogais (maiúsculas e minúsculas)
    vogais = 'aeiouAEIOU'
    # Inicializar o contador de vogais em zero
    contador = 0
    # Percorrer cada caractere no texto fornecido
    for letra in texto:
        # Verificar se o caractere atual é uma vogal
        if letra in vogais:
            # Se for vogal, incrementar o contador em 1
            contador += 1
    # Retornar o total de vogais encontradas no texto
    return contador

# Exemplo de uso da função
# Definir uma string para testar a função
texto_teste = "Olá, mundo! Este é um exemplo de contador de vogais."

# Chamar a função contar_vogais passando o texto de teste
numero_de_vogais = contar_vogais(texto_teste)

# Imprimir o resultado na tela
print(f"O número de vogais no texto é: {numero_de_vogais}")
