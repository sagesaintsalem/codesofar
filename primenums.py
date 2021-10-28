def is_prime(num):
    if num == 2 or num == 3 or num == 5 or num == 7:
        return True
    elif num % 2 == 0 or num % 3 == 0 or num % 4 == 0 or num % 5 == 0 or num % 7 == 0:
        return False
    else:
        return True


for i in range(1, 20):
	if is_prime(i + 1):
			print(i + 1, end=" ")
print()


def betterFun(num):
    hecc = int(num ** 0.5)
    for i in range(2, (hecc + 1)):
        if num % i == 0:
            return False
    return True
        
print("Alternatively - ")
for i in range(1, 20):
	if betterFun(i + 1):
			print(i + 1, end=" ")
print()
