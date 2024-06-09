from exercises import CompararGastos

def test_adicionar_gastos_joao():
    comparador = CompararGastos.ComparadorDeGastos()
    comparador.adicionar_gastos_joao(300)
    comparador.adicionar_gastos_joao(500)
    comparador.adicionar_gastos_joao(200)
    comparador.adicionar_gastos_joao(800)
    assert comparador.gastos_joao == [300, 500, 200, 800]

def test_adicionar_gastos_pedro():
    comparador = CompararGastos.ComparadorDeGastos()
    comparador.adicionar_gastos_pedro(200)
    comparador.adicionar_gastos_pedro(400)
    comparador.adicionar_gastos_pedro(500)
    comparador.adicionar_gastos_pedro(700)
    assert comparador.gastos_pedro == [200, 400, 500, 700]

def test_calcular_total_gastos():
    comparador = CompararGastos.ComparadorDeGastos()
    total = comparador.calcular_total_gastos([300, 500, 200, 800])
    assert total == 1800

def test_quem_gastou_mais_joao():
    comparador = CompararGastos.ComparadorDeGastos()
    comparador.adicionar_gastos_joao(300)
    comparador.adicionar_gastos_pedro(200)
    comparador.adicionar_gastos_joao(500)
    comparador.adicionar_gastos_pedro(400)
    comparador.adicionar_gastos_joao(200)
    comparador.adicionar_gastos_pedro(100)
    maior_gastador = comparador.quem_gastou_mais()
    assert maior_gastador == "João"

def test_quem_gastou_mais_pedro():
    comparador = CompararGastos.ComparadorDeGastos()
    comparador.adicionar_gastos_joao(300)
    comparador.adicionar_gastos_pedro(200)
    comparador.adicionar_gastos_joao(500)
    comparador.adicionar_gastos_pedro(400)
    comparador.adicionar_gastos_joao(200)
    comparador.adicionar_gastos_pedro(600)
    maior_gastador = comparador.quem_gastou_mais()
    assert maior_gastador == "Pedro"

def test_quem_gastou_mais_empate():
    comparador = CompararGastos.ComparadorDeGastos()
    comparador.adicionar_gastos_joao(300)
    comparador.adicionar_gastos_pedro(300)
    comparador.adicionar_gastos_joao(500)
    comparador.adicionar_gastos_pedro(500)
    comparador.adicionar_gastos_joao(600)
    comparador.adicionar_gastos_pedro(600)
    maior_gastador = comparador.quem_gastou_mais()
    assert maior_gastador == "Empate"
