from funciones import sumar
from funciones import es_primo

def test_sumar():
    assert sumar(2,4) == 6
    assert sumar(-2,2) == 0
    assert sumar(2,2) == 4

def test_es_primo():
    assert es_primo(7) is True
    assert es_primo(6) is False
    assert es_primo(3) is True
    assert es_primo(11) is True
    assert es_primo(9) is False
    assert es_primo(4) is False
