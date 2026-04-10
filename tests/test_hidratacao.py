import pytest
import os
from src.hidratacao import RastreadorAgua

@pytest.fixture
def rastreador():
    """Prepara um ambiente de teste isolado com um arquivo temporário."""
    arquivo_teste = 'teste_agua.json'
    r = RastreadorAgua(arquivo=arquivo_teste)
    r.dados = {"total_ml": 0, "registros": [], "meta": 0} 
    yield r
    if os.path.exists(arquivo_teste):
        os.remove(arquivo_teste)

def test_definir_perfil(rastreador):
    """Valida o cálculo de meta diária para perfis sedentários e ativos."""
    rastreador.definir_perfil(70, pratica_esporte=False)
    assert rastreador.obter_meta() == 2450 # 70kg * 35ml
    
    rastreador.definir_perfil(70, pratica_esporte=True)
    assert rastreador.obter_meta() == 3500 # 70kg * 50ml

def test_adicionar_agua_caminho_feliz(rastreador):
    """Valida a adição de consumo e o cálculo do volume faltante."""
    rastreador.definir_perfil(70, pratica_esporte=False) # Meta será 2450ml
    msg = rastreador.adicionar_agua(250)
    
    assert rastreador.obter_total() == 250
    assert "Faltam 2200ml" in msg
    assert "Registro adicionado" in msg

def test_adicionar_agua_valor_negativo(rastreador):
    """Garante que o sistema rejeita entradas com valores negativos."""
    rastreador.definir_perfil(70, pratica_esporte=False)
    with pytest.raises(ValueError, match="maior que zero"):
        rastreador.adicionar_agua(-50)

def test_atingir_meta(rastreador):
    """Valida a mensagem de sucesso ao atingir ou ultrapassar a meta."""
    rastreador.definir_perfil(60, pratica_esporte=False) # Meta será 2100ml
    rastreador.adicionar_agua(2000)
    msg = rastreador.adicionar_agua(100) 
    
    assert "Parabéns, você atingiu a meta diária" in msg
    assert rastreador.obter_total() == 2100