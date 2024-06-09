from exercises import IndiceAlfabeto

def test_indice_para_letra_valido():
    alfabeto = IndiceAlfabeto.Alfabeto()
    assert alfabeto.indice_para_letra(1) == "A"
    assert alfabeto.indice_para_letra(26) == "Z"
    assert alfabeto.indice_para_letra(5) == "E"
    assert alfabeto.indice_para_letra(10) == "J"
    assert alfabeto.indice_para_letra(20) == "T"

def test_indice_para_letra_invalido():
    alfabeto = IndiceAlfabeto.Alfabeto()
    assert alfabeto.indice_para_letra(0) == ""
    assert alfabeto.indice_para_letra(27) == ""
    assert alfabeto.indice_para_letra(-1) == ""
    assert alfabeto.indice_para_letra(100) == ""

def test_indice_para_letra_limite():
    alfabeto = IndiceAlfabeto.Alfabeto()
    assert alfabeto.indice_para_letra(1) == "A"
    assert alfabeto.indice_para_letra(26) == "Z"