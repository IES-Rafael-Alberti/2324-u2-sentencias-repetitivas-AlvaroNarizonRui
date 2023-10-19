from src.ejercicio3 import numerosImpares
import pytest

def testImpares():
    assert numerosImpares(3) == "1,3,"
    assert numerosImpares(10) == "1,3,5,7,9,"
    assert numerosImpares(20) == "1,3,5,7,9,11,13,15,17,19,"
    assert numerosImpares(4) == "1,3,"
if __name__ == "__main__":
    pytest.main()