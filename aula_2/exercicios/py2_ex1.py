# py2_ex1.py
def soma(*args):
    """
    Aceita um número variável de argumentos e retorna a soma deles.
    
    Parâmetros:
        *args (int, float): números a serem somados.
    
    Retorna:
        float: A soma dos números fornecidos.
    """
    return sum(args)

# Exemplo de uso
if __name__ == "__main__":
    resultado = soma(1, 2, 3, 4, 5)
    print("Soma dos valores:", resultado)
