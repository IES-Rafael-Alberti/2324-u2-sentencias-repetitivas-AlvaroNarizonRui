from src.ejercicio6 import creadorTriangulo
import pytest

def testTriangulo():
    assert creadorTriangulo(5) == "*" + "\n" + "**" + "\n" + "***" + "\n" + "****" + "\n" + "*****" + "\n"
    assert creadorTriangulo(3) == "*" + "\n" + "**" + "\n" + "***" + "\n"
    assert creadorTriangulo(0) == "Error"
    assert creadorTriangulo(-1) == "Error"

if __name__ == "__main__":
    pytest.main()