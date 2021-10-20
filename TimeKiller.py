print("Welcome to the Time Killer! Answer Y or N to the following to figure out what to do today!")
while(True):
    today = str(input("Is there anything that could be cleaned or tidied? "))

    if today == "N" or today == "n":
        print("OK, let's think of something else!")
        today = str(input("Are there any errands you need to run? "))
        if today == "N" or today == "n":
            print("OK, what else?")
            today = str(input("Can you walk or exercise today? "))
            if today == "N" or today == "n":
                print("That's ok!")
                today = str(input("Peux-tu etudier francais? "))
                if today == "N" or today == "n":
                    print("D'accord...")
                    today = str(input("Got a knitting or crochet project to work on? "))
                    if today == "N" or today == "n":
                        print("Man, you're on top of it today aren'cha???")
                        today = str(input("Well, do you fancy coding or homework? "))
                        if today == "N" or today == "n":
                            print("I dunno then...Netflix? Games? Time is your plaything. Hit 'x' to quit. ")
                            today = str(input())
                            if today == "x" or today == "X":
                                break
else:
    print("Alright! Go do that then!")
