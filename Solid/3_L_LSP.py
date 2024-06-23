# O Princípio de Substituição de Liskov (LSP) é uma diretriz crucial no design orientado a objetos, 
# que reforça a importância de garantir que as subclasses permaneçam compatíveis com o comportamento de suas classes base. 

class Bird:
    def fly(self):
        print("This bird can fly.")

class Sparrow(Bird):
    def fly(self):
        print("Sparrow flying.")

class Ostrich(Bird):
    def fly(self):
        raise Exception("Ostriches cannot fly!")

def make_bird_fly(bird: Bird):
    bird.fly()

# Testando o código
sparrow = Sparrow()
make_bird_fly(sparrow)  # Funciona como esperado

ostrich = Ostrich()
make_bird_fly(ostrich)  # Levanta uma exceção, violando o princípio de Liskov
