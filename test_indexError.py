import pytest
from indexError import lista


def test_listaCorrecto():
    assert lista(2) == "Pera"
    assert lista(0) == "Manzana"



def test_listaError():
    assert lista(3) == IndexError





