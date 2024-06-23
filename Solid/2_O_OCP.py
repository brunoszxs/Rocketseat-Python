# O Princípio Aberto-Fechado (OCP) afirma que as entidades de software (classes, módulos, funções, etc.) devem estar abertas para extensão, 
# mas fechadas para modificação.  

# Esse princípio permite que o comportamento de uma entidade de software seja estendido sem alterar o código existente, 
# o que ajuda a evitar bugs e facilita a manutenção.

class Programmer:
    def make(self):
        print("Programmer creating code")
        
class Cybersecurity:
    def make(self):
        print("Protect for Plataform Cyber EDR/AV/Siem")

class Company:
    def do_work(self, worker: any) -> None:
        worker.make()

programmer = Programmer()
cybersecurity = Cybersecurity()
company = Company()

company.do_work(programmer)
company.do_work(cybersecurity)