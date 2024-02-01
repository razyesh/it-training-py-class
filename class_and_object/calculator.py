class Calculator:
    def __init__(self, num1, num2) -> None:
        self.num1 = num1
        self.num2 = num2

    def addition(self): # polymorphism
        return self.num1 + self.num2


abcd = int(input("Enter number1: "))
number2 = int(input("Enter number 2: "))

c = Calculator(abcd, number2)
c.num1
c.num2