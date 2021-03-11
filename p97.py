#number guessing game
import random
print("number guessing game")
number=random.randint(1,20)
chances=0
print("Guess a number between 1 to 20")
while chances<3:
    guess=int(input("enter your guess"))
    if guess==number:
        print("congratulation you won!")
    elif guess<number:
        print("your guess was too low, guess a high number:)")
    else:
        print("your guess was too high, guess a lower number:)")
    chances+=1

if not chances<3:
    print("you loose,the number is",number)