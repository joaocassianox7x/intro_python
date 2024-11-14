# py2_ex5.py
import functools

def cache_results(func):
    """
    Decorador para armazenar resultados de função em cache e reutilizá-los para chamadas com os mesmos argumentos.
    
    Utiliza um dicionário como cache onde as chaves são os argumentos e os valores são os resultados.
    """
    cache = {}

    @functools.wraps(func)
    def wrapper(*args):
        if args in cache:
            print("Usando cache para:", args)
            return cache[args]  # Retorna resultado do cache
        else:
            result = func(*args)  # Calcula resultado
            cache[args] = result  # Armazena no cache
            return result
    return wrapper

# Exemplo de uso
@cache_results
def soma(a, b):
    return a + b

if __name__ == "__main__":
    print(soma(5, 10))
    print(soma(5, 10))  # Resultado do cache
    print(soma(2, 3))
