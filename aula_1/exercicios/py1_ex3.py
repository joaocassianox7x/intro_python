# Jogo Pedra, Papel, Tesoura
import random

def pedra_papel_tesoura():
    # Opções disponíveis
    opcoes = ['Pedra', 'Papel', 'Tesoura']

    # Solicita a escolha do jogador
    jogador = input("Escolha Pedra, Papel ou Tesoura: ").capitalize()

    # Verifica se a escolha é válida
    if jogador not in opcoes:
        print("Escolha inválida! Tente novamente.")
        return

    # Escolha aleatória do computador
    computador = random.choice(opcoes)

    # Exibe as escolhas
    print(f"Você escolheu: {jogador}")
    print(f"O computador escolheu: {computador}")

    # Determina o vencedor
    if jogador == computador:
        print("Empate!")
    elif (jogador == 'Pedra' and computador == 'Tesoura') or \
         (jogador == 'Papel' and computador == 'Pedra') or \
         (jogador == 'Tesoura' and computador == 'Papel'):
        print("Você ganhou!")
    else:
        print("Você perdeu!")

# Exemplo de uso da função
pedra_papel_tesoura()
