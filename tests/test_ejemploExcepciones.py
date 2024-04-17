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


def test_fileNotFoundError():
    ejemplo = EjemploExecpciones()
    with pytest.raises(FileNotFoundError):
        ejemplo.fileNotFoundError("hola.txt")


def test_indexError():
    ejemplo = EjemploExecpciones()
    with pytest.raises(IndexError):
        ejemplo.indexError(8)

    assert ejemplo.indexError(0) == "Manzana"



def test_permissionError():
    ejemplo = EjemploExecpciones()
    with pytest.raises(PermissionError):
        ejemplo.permissionError()