from src.ejercicio7 import tablaMultiplicar
import pytest

def testMultiplicar():
    resultado_esperado = ""
    for i in range(10):
        for j in range(11):
            resultado_esperado += str(i) + " x " + str(j) + " = " + str(i*j) + "\n"
    assert tablaMultiplicar() == resultado_esperado

if __name__ == "__main__":
    pytest.main()