# O Princípio da Responsabilidade Única (SRP) declara que uma classe deve ter apenas uma razão para mudar.
# Esse princípio ajuda a manter as classes coesas, facilitando a manutenção e a compreensão do código.

class Process:
    def handle(self, username: str, password: str) -> None:
        if self._verify_input_data(username, password):
            self._verify_input_in_database(username)
            self._insert_new_user(username, password)
        else:
            self._raise_error('Dados Inválidos')

    def _verify_input_data(self, username: str, password: str) -> bool:
        return isinstance(username, str) and isinstance(password, str)

    def _verify_input_in_database(self, username: str) -> None:
        print('Acessando o banco de dados...')
        print('Verificando existência do usuário...')

    def _insert_new_user(self, username: str, password: str) -> None:
        print('Cadastro de usuários realizado com sucesso!')

    def _raise_error(self, message: str) -> Exception:
        raise Exception(message)
