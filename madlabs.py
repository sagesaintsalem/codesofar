def given(a):
    return a


roygbiv = str(input("Enter a colour: "))
#roygbiv2 = str(input("Another colour: "))
#roygbiv3 = str(input("And another: "))
descrip = str(input("Enter an adjective: "))
descrip2 = str(input("Enter a second adjective: "))
#descrip3 = str(input("And another: "))
#descrip4 = str(input("One more: "))
#doing = str(input("Give me a verb: "))
done = str(input("Give me a past tense verb: "))
thing = str(input("Give me a noun: "))
thing2 = str(input("A second noun: "))
#thing3 = str(input("A third noun: "))
#thing4 = str(input("A fourth: "))
#thing5 = str(input("One more: "))
thing6 = int(input("Lastly, what's your lucky number?: "))


print("The sky was", given(roygbiv), "and the ground was",
      given(descrip), ". \nI woke up on a", given(thing), "and felt very",
      given(descrip2), "because I had", given(done), "\non the", given(thing2), given(thing6), "times!") 
