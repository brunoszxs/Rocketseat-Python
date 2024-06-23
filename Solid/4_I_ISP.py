# O Princípio de Segregação de Interface (ISP) sugere que nenhuma classe deve ser forçada a implementar interfaces que não utilizará. 
# Isso impede que uma interface se torne "inchada", com métodos que não são relevantes para todas as suas classes implementadoras. 

from abc import ABC, abstractmethod

class Printer(ABC):
    @abstractmethod
    def print_document(self, document):
        pass

class Scanner(ABC):
    @abstractmethod
    def scan_document(self):
        pass

class Photocopier(Printer, Scanner):
    def print_document(self, document):
        print(f"Printing: {document}")

    def scan_document(self):
        return "Scanned document"

class SimplePrinter(Printer):
    def print_document(self, document):
        print(f"Printing simple: {document}")

# Usando as interfaces segregadas
photocopier = Photocopier()
photocopier.print_document("My Document")
result = photocopier.scan_document()
print(result)

simple_printer = SimplePrinter()
simple_printer.print_document("Another Document")
