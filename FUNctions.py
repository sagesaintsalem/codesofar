def add(a, b):
    return a + b

def minus(a, b):
    return a - b

def times(a, b):
    return a*b

def divi(a, b):
    return a/b

def square(a):
    return a*a

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

print("Added together, you get", add(x, y))
print("Subtracted, you get", minus(x, y))
print("Multiplied together, you get", times(x, y))
print("Divided, you get", divi(x, y))

z = int(input("Enter a new number: "))

print(z, "squared is", square(z))
