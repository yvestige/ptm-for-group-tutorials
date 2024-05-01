choice = 1
num1 = 0
num2 = 0
while choice !=5:
    print("Area Calculator")
    print("[1] Square")
    print("[2] Rectangle")
    print("[3] Triangle")
    print("[4] Circle")
    print("[5] Exit")
    choice = int(input("Enter number:\t"))
    if choice == 1:
        num1 = float(input("Enter length of side:\t"))
        res = num1 * num1
        print("The area of square is:", res)
    elif choice == 2:
        num1 = float(input("Enter length of rectangle:\t"))
        num2 = float(input("Enter width of rectangle:\t"))
        res = num1 * num2
        print("The area of rectangle is:", res)
    elif choice == 3:
        num1 = float(input("Enter base of triangle\t"))
        num2 = float(input("Enter height of triangle:\t"))
        res = num1 * num2 / 2
        print("The area of triangle is:", res)
    elif choice == 4:
        num1 = float(input("Enter radius of circle:\t"))
        res = 3.14 * num1 * num1
        print("The area of circle is:", res)
    elif choice == 5:
        print("Thank you for using the Area calculator")
    else:
        print("Please enter a number from 1 to 5 only!")