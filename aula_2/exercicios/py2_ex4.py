# py2_ex4.py
class ContaBancaria:
    """
    Classe para gerenciar saldo bancário com métodos privados.
    
    Métodos:
        depositar(valor): Depósito de valor no saldo.
        sacar(valor): Retirada de valor do saldo.
    """
    
    def __init__(self, saldo_inicial=0):
        self._saldo = saldo_inicial  # Atributo de saldo privado

    def _adicionar_saldo(self, valor):
        """Método privado para adicionar valor ao saldo."""
        self._saldo += valor
    
    def _remover_saldo(self, valor):
        """Método privado para remover valor do saldo, se possível."""
        if valor <= self._saldo:
            self._saldo -= valor
        else:
            print("Saldo insuficiente.")

    def depositar(self, valor):
        """Método público para depositar valor, chamando o método privado."""
        self._adicionar_saldo(valor)
        print(f"Depósito realizado. Saldo atual: {self._saldo}")

    def sacar(self, valor):
        """Método público para sacar valor, chamando o método privado."""
        self._remover_saldo(valor)
        print(f"Saque realizado. Saldo atual: {self._saldo}")

# Exemplo de uso
if __name__ == "__main__":
    conta = ContaBancaria(100)
    conta.depositar(50)
    conta.sacar(30)
    conta.sacar(150)
