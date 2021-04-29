def calc(a, b):
    add = a + b
    subtract = a - b
    mult = a * b
    divide = a / b
    print(str(a) + " + " + str(b) + " = " + str(add))
    print(str(a) + " - " + str(b) + " = " + str(subtract))
    print(str(a) + " * " + str(b) + " = " + str(mult))
    print(str(a) + " / " + str(b) + " = " + str(divide))


def userInput():
    print("Enter the first integer: ", end="")
    num1 = int(input())
    print("Enter the second integer: ", end="")
    num2 = int(input())
    print("")
    calc(num1,num2)

