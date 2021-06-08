# def hello(name):
#     print(f"hello, {name}")

# hello("pratama") 

# def hello(name: str, age:int):
#     return f"hello, {name}, i`m {age}"

# argument = hello("pratama", 23)

# print(argument)

def min_plus_mod(num1: int, num2 : int):
    min = num1 - num2
    plus = num1 + num2
    mod = num1 % num2

    return min,plus, mod

minus,plus, modulus = min_plus_mod(10,2)

print(minus,plus, modulus)
