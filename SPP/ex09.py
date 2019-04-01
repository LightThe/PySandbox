# Write a guessing game where the user has to guess a secret number.

x=53
tries=1
guess = int(input("type in a number: "))
while guess!=x :
    if guess>x :
        print("The number you typed is higher")
    else:
        print("The number you typed is lower")
    old=guess
    guess = int(input("type in a number: "))
    if guess!=old : tries+=1
print("You got it on the first try!") if tries==1 else print("You made it in "+str(tries)+" tries")

