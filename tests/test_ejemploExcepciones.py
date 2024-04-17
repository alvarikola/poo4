import pytest

from ejemploExcepciones import EjemploExecpciones

def test_ZeroDivisionError():
    ejemplo = EjemploExecpciones()
    with pytest.raises(ZeroDivisionError):
        ejemplo.zeroDivisionError(num = 2, den = 0)

    assert ejemplo.zeroDivisionError(num = 4, den = 2)