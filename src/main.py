class Calculator:
    pass


from src.main import Calculator

def test_division():
    calculator = Calculator()
    assert calculator.divide(3, "2") == 1.5