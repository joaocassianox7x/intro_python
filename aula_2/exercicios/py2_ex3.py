# py2_ex3.py
import functools

def log_function_calls(func):
    """
    Decorador para registrar chamadas de função, seus argumentos e retorno em um arquivo de log.
    
    O log será gravado no arquivo 'log.txt'.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Chamada e resultado da função
        result = func(*args, **kwargs)
        
        # Log da chamada da função
        with open("log.txt", "a") as log_file:
            log_file.write(f"Função: {func.__name__}\n")
            log_file.write(f"Args: {args}, Kwargs: {kwargs}\n")
            log_file.write(f"Retorno: {result}\n")
            log_file.write("-" * 40 + "\n")
        
        return result
    return wrapper

# Exemplo de uso
@log_function_calls
def exemplo_funcao(a, b):
    return a + b

if __name__ == "__main__":
    print("Resultado da função exemplo:", exemplo_funcao(5, 10))
