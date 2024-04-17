import pytest

from ejemploExcepciones import EjemploExecpciones

def test_ZeroDivisionError():
    ejemplo = EjemploExecpciones()
    with pytest.raises(ZeroDivisionError):
        ejemplo.zeroDivisionError(num = 2, den = 0)

    assert ejemplo.zeroDivisionError(num = 4, den = 2) == 2


def test_ValueError():
    ejemplo = EjemploExecpciones()
    with pytest.raises(ValueError):
        ejemplo.valueError(1, "h")