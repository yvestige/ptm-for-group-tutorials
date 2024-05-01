# # def mult(num1, num2):
# #     return num1*num2

# # print(5*mult(2,mult(3,4)))

# def hello():
#     print("Hello", end = " ")
#     world()

# def world():
#     print("world")

# hello()

# def exp(base,)

def exp(base,pow):
    if pow == 0: return 1
    elif pow == 1: return base
    else: return base*exp(base,pow-1)

print(exp(2,2))
print(exp(3,3))