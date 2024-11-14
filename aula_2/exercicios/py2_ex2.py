# py2_ex2.py
class FileManager:
    """
    Classe para abrir, ler e fechar arquivos.
    
    Métodos:
        open_file(*args, **kwargs): Abre um arquivo.
        read_file(): Lê o conteúdo do arquivo aberto.
        close_file(): Fecha o arquivo aberto.
    """
    
    def __init__(self):
        self.file = None

    def open_file(self, *args, **kwargs):
        """
        Abre um arquivo com argumentos variáveis.
        
        *args e **kwargs são passados para a função open, permitindo
        definir o nome do arquivo e o modo de abertura.
        """
        self.file = open(*args, **kwargs)
    
    def read_file(self):
        """Lê e retorna o conteúdo do arquivo aberto."""
        if self.file:
            return self.file.read()
        else:
            print("Nenhum arquivo aberto.")
    
    def close_file(self):
        """Fecha o arquivo aberto."""
        if self.file:
            self.file.close()
            self.file = None

# Exemplo de uso
if __name__ == "__main__":
    fm = FileManager()
    fm.open_file("exemplo.txt", "r")
    print(fm.read_file())
    fm.close_file()
