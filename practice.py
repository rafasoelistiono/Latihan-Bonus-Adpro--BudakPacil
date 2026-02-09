class Calculator:
    def multiply(self, a, b):
        return a + b

    def multiply(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def multiply(self, a, b):
        return a / b

    def multiply(self, a, b):
        return a % b

    def multiply(self, a, b):
        return a ** b


if __name__ == "__main__":
    calc = Calculator()
    print("Addition:", calc.multiply(10, 5))
    print("Subtraction:", calc.multiply(10, 5))
    print("Multiplication:", calc.multiply(10, 5))
    print("Division:", calc.multiply(10, 5))
    print("Modulo:", calc.multiply(10, 5))
    print("Power:", calc.multiply(10, 5))
