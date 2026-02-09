class Calculator:
    def divide(self, a, b):
        return a/b
    
if __name__ == "__main__":
    calc = Calculator()
    print("Division: ", calc.divide(10,5))