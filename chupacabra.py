safeword = "chupacabra"
counter = 0
word = str(input("I'm gonna eat your words! Gimme a word! "))
counter += 1

while word != safeword:
    print("Om nom nom!")
    word = str(input("MOAR!!! "))
    counter += 1
    if counter == 5:
        print("Miam! Thank you for your words!")
        break
else:
    print("Oh no! Poison! You've killed me uwu")
    
