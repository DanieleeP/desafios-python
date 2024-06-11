class Alfabeto:
    def __init__(self):
        self.letras = [chr(i) for i in range(65,91)]

    def indice_para_letra(self, indice):
        if 1 <= indice <= 26:
            return self.letras[indice - 1]
        else:
            return ''