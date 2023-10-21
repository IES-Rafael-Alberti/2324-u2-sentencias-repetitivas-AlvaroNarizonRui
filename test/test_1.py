from src.ejercicio1 import  mostrarPalabra
import pytest

def testmostrarPalabra():
    assert mostrarPalabra("paco",10) == ("paco" + "\n") * 10
    assert mostrarPalabra("Eduardo",10) == ("Eduardo" + "\n") * 10
if __name__ == "__main__":
    pytest.main()