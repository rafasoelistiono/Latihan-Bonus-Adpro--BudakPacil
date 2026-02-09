class Calculator:
    def power(self, a, b):
        return a + b

    def power(self, a, b):
        return a - b

    def power(self, a, b):
        return a * b

    def power(self, a, b):
        return a / b

    def power(self, a, b):
        return a % b

    def power(self, a, b):
        return a ** b


if __name__ == "__main__":
    calc = Calculator()
    print("Addition:", calc.power(10, 5))
    print("Subtraction:", calc.power(10, 5))
    print("Multiplication:", calc.power(10, 5))
    print("Division:", calc.power(10, 5))
    print("Modulo:", calc.power(10, 5))
    print("Power:", calc.power(10, 5))