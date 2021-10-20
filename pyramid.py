blocks = int(input("Enter the number of blocks: "))

height = 1

while(blocks - height >= 0):
    blocks = blocks - height
    height += 1
    if (blocks - height < 0):
        height -= 1
        break
    elif (blocks - height == 0):
        break

print("The height of the pyramid:", height)
