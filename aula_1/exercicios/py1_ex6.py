# Função para classificar a idade de acordo com categorias predefinidas
def classificar_idade(idade):
    # Verifica se a idade está em uma categoria específica
    if idade < 0:
        return "Idade inválida"
    elif idade <= 12:
        return "Criança"
    elif idade <= 17:
        return "Adolescente"
    elif idade <= 64:
        return "Adulto"
    else:
        return "Idoso"

# Exemplo de uso:
idades = [3, 15, 30, 70, -5]
for idade in idades:
    classificacao = classificar_idade(idade)
    print(f"Idade {idade}: {classificacao}")
