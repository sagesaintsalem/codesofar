c0 = int(input("Enter a number greater than 1: "))
count = 0


while c0 != 1:
    if c0 % 2 == 0:
        c0 /= 2
        print(int(c0))
        count += 1
    else:
        c0 = 3 * c0 + 1
        print(int(c0))
        count += 1
else: print("Steps:", count)
