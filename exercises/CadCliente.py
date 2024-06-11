class Cliente:
    def __init__(self, nome, telefone, email):
       
       self.nome = nome
       self.telefone = telefone
       self.email = email

    def exibir_informacoes(self):
       return f"Nome: {self.nome}\nTelefone: {self.telefone}\nEmail: {self.email}"

    