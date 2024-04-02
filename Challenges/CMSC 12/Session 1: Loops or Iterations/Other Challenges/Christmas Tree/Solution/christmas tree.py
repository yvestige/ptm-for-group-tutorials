

n = int(input("Value of n: "))

print(" ")


# print the tree leaves or smth
for i in range(n):
    
    # print yung space sa left
    for j in range((2*n)-(i)):
        print(" ", end='')
    
    # prints yung numbers na naka-ano sa left
    for j in range(i+1)[::-1]:
        print(f"{j+1} ", end='')

    
    # prints yung numbers na naka-ano sa right
    for j in range(i+1):
        if (j <= i+1): 
            continue
        else:
            print(f"{j+1} ", end='')
    
    
    # print yung space sa right
    for j in range((2*n)-(i)):
        print(" ", end='')
    print("")


# print the base
for i in range(n):
    
    # break if already beyond 1
    if (i != 0): break
    
    # print yung space sa left
    for j in range((2*n)-(i)):
        print(" ", end='')
    
    # print the base
    print("| ", end='')
    
    # print yung space sa right 
    for j in range((2*n)-(i)):
        print(" ", end='')
    print("")


print(" ")