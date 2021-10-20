nummers = range(1, 101)

for i in nummers:
    if i % 3 == 0 and i % 5 ==0:
        print(" Fizzbuzz ", end=" ")
    elif i % 3 == 0:
        print(" Fizz ", end=" ")
    elif i % 5 ==0:
        print(" Buzz ", end=" ")
    else:
        print(i, end=" ")

