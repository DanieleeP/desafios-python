from exercises import CadCliente

def test_CadCliente():
    cliente = CadCliente.Cliente('Fulano', '1234-5678', 'fulano@email.com')
    assert cliente.nome == 'Fulano'
    assert cliente.telefone == '1234-5678'
    assert cliente.email == 'fulano@email.com'
    assert cliente.exibir_informacoes() == "Nome: Fulano\nTelefone: 1234-5678\nEmail: fulano@email.com"

