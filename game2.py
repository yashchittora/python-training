from random import *

ch = int(input("Enter number of chances : "))

cn = randint(1,100)

for i in range(1,ch+1):
    un = int(input("Enter your number : "))

    if un == cn:
        print("You guessed it right !!!")
        break
    
    elif un > cn:
        print("No my number is smaller than",un)
    
    elif cn > un:
        print("No my number is greater than",un)
    
if i == ch:
    print("Lol you Loser ^_^")

