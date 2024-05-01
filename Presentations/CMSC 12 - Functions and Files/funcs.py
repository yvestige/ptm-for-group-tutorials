def area(num1, num2):
    return num1 * num2

def inputNumbers():
    num1 = float(input("Enter number 1:\t"))
    num2 = float(input("Enter number 2:\t"))
    return [num1, num2]

def printMenu():
    print("[1] Square")
    print("[2] Rectangle")
    print("[3] Triangle")
    print("[4] Circle")
    print("[5] Exit")