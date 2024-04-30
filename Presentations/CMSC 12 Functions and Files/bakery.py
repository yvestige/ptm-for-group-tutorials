def save():
    file = open("basket.txt", "w")
    data = ""
    for food in basket:
        line = food + "," + str(basket[food]) + "\n"
        data = data + line

    file.write(data)
    file.close()

def load():
    file = open("basket.txt", "r")
    for line in file.readlines():
        line = line.split(",")
        basket[line[0]] = float(line[1])
    
    file.close()

def printMenu():
    print("Welcome to Roco Bakery!")
    print("[1] Buy Baked Goods")
    print("[2] Buy Pastries")
    print("[3] Remove an item from the basket")
    print("[4] Pay for the items in the basket")
    print("[5] Exit")

def printBakedGoods():
    print("List of Baked Goods:")
    print("[1] Pandesal \t(P2.00)")
    print("[2] Maligaya \t(P3.00)")
    print("[3] Crinkles \t(P3.00)")
    print("[4] Spanish bread \t(P3.50)")
    print("[5] Croissant \t(P5.00)")
    print("[6] Return")

def printPastries():
    print("List of Pastries")
    print("[1] Cheesecake \t(P149.75)")
    print("[2] Chocolate cake \t(P124.50)")
    print("[3] Chiffon cake \t(P99.50)")
    print("[4] Red velvet cake \t(P199.75)")
    print("[5] Black forest cake \t(P249.50)")
    print("[6] Return")


basket = {"total":0}
foods = ["pandesal", "maligaya", "crinkles", "spanish bread", "croissant",
          "cheesecake", "chocolate cake", "chiffon cake", "red velvet cake",
          "black forest cake"]
prices = {"pandesal":2.00, "maligaya":3.00, "crinkles": 3.00, "spanish bread":3.50, "croissant":5.00,
          "cheesecake":149.75, "chocolate cake":124.50, "chiffon cake":99.50, "red velvet cake":199.75,
          "black forest cake":249.50}

def pick(offset):
    choice2 = int(input("Which baked goods would you like to buy?\t"))
    if choice2 == 6:
        print("Returning to main menu")
    elif choice2 > 0 and choice2 < 6:
        food = foods[choice2+offset]
        add(food, prices[food])
    else:
        print("Please input numbers 1-6 only!")

def add(food,cost):
    qty = int(input("How many are you going to buy:\t"))
    total = cost*qty
    basket[food] = qty
    basket["total"] += total
    print("Added",food,"into your basket, adding",total,"into your fees.")
    print("You now have an outstanding fee of",basket["total"],".")

def remove():
    for food in basket:
        if food == "total":
            continue
        print(food,basket[food],"pieces")
    
    choice = input("Which food are you going to remove?\t").lower()
    if choice in basket:
        qty = int(input("How many pieces are you going to remove?"))
        if qty < basket[choice]:
            basket[choice] -= qty
            basket["total"] -= qty*prices[choice]
            print("Successfully removed",qty,"pieces of",choice, "from your basket!")
            print("You now have an outstanding fee of",basket["total"],".")
        elif qty == basket[choice]:
            basket.pop(food)
            basket["total"] -= qty*prices[choice]
            print("You now have an outstanding fee of",basket["total"],".")
            print("Successfully removed",choice,"from your basket!")
        else:
            print("Please input a number lower or equal to the quantity of the food in your basket!")

    else:
        print("Please input a food from the list!")

def pay():
    if(basket["total"] == 0):
        print("There is nothing inside the basket.")
        return
    
    for food in basket:
        if food == "total":
            continue
        print(food,basket[food],"pieces")
    print("For a total of:",basket["total"])
    money = 0
    while money < basket["total"]:
        money = float(input("How many cash do you have in hand?\t"))
        if money < basket["total"]:
            print("Not enough money, you need",basket["total"],"or more")

    money = basket["total"]
    basket.clear()
    basket["total"] = 0

    print("Successfully paid for the items!")
    print("You have a change of",money)

load()
choice = 0
while choice != 5:
    printMenu()
    choice = int(input("Enter number from 1-5:\t"))
    if choice == 1:
        printBakedGoods()
        pick(-1)
    elif choice == 2:
        printPastries()
        pick(5)
    elif choice == 3:
        remove()
    elif choice == 4:
        pay()
    elif choice == 5:
        print("Thank you for shopping with us!")
        save()
    else:
        print("Please input numbers 1-5 only!")