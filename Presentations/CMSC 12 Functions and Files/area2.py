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



choice = 1
nums = []
res = 0
while choice !=5:
    print("Area Calculator")
    printMenu()
    choice = int(input("Enter number:\t"))
    if choice == 1:
        num1 = float(input("Enter length of side:\t"))
        res = area(num1, num1)
        print("The area of square is:", res)
    elif choice == 2:
        nums = inputNumbers()
        res = area(nums[0], nums[1])
        print("The area of rectangle is:", res)
    elif choice == 3:
        nums = inputNumbers()
        nums[1] = nums[1] / 2
        res = area(nums[0], nums[1])
        print("The area of triangle is:", res)
    elif choice == 4:
        num1 = float(input("Enter radius of circle:\t"))
        num1 = num1 * num1
        res = area(3.14, num1)
        print("The area of circle is:", res)
    elif choice == 5:
        print("Thank you for using the Area calculator")
    else:
        print("Please enter a number from 1 to 5 only!")