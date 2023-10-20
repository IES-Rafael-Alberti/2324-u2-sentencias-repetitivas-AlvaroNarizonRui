from src.ejercicio5 import calculadoraInteres
import pytest
def testInteres():
    assert calculadoraInteres(3,25,1500) == ['1875', '4218', '13708', '']
    assert calculadoraInteres(1,3,5000) == ['5150', '']
    assert calculadoraInteres(5,50,1000) == ['1500', '3750', '13125', '59062', '324841', '']
if __name__ == "__main__":
    pytest.main()