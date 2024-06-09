from exercises import AumentoPercentual

def test_definir_aumento_vendas():
    loja = AumentoPercentual.FormatarPercentual()
    loja.definir_aumento_vendas(32.048701)
    assert loja.aumento_vendas == 32.048701

def test_exibir_aumento_formatado():
    loja = AumentoPercentual.FormatarPercentual()
    loja.definir_aumento_vendas(32.048701)
    resultado = loja.exibir_aumento_formatado()
    assert resultado == "O aumento percentual de vendas foi de 32.05%"

def test_exibir_aumento_formatado_zero():
    loja = AumentoPercentual.FormatarPercentual()
    loja.definir_aumento_vendas(0.0)
    resultado = loja.exibir_aumento_formatado()
    assert resultado == "O aumento percentual de vendas foi de 0.00%"