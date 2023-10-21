from src.ejercicio4 import cuentaAtras
import pytest

def testcuentaAtras():
    assert cuentaAtras(5) == "5,4,3,2,1,0"
    assert cuentaAtras(1) == "1,0"
    assert cuentaAtras(0) == "Error"
    assert cuentaAtras(-1) == "Error"
    assert cuentaAtras(10) == "10,9,8,7,6,5,4,3,2,1,0"

if __name__ == "__main__":
    pytest.main()