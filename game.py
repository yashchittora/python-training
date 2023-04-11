from random import *

l = ['r','p','s']

chances = 10
usrSc = 0
compSc = 0
draw = 0

for i in range(chances):
    print("\nChance Number",i+1)
    
    u = input("Enter choice : ")

    c = choice(l)
    print("Computer's Choice : ",c)

    if u.lower()=='r' and c=='p':
        compSc+=1
        print("Point goes to Computer")
    elif u.lower()=='r' and c=='r':
        print("Draw")
        draw+=1
    elif u.lower()=='r' and c=='s':
        usrSc+=1
        print("Point goes to You")
 
    elif u.lower()=='s' and c=='s':
        print("Draw")
        draw+=1
    elif u.lower()=='s' and c=='p':
        usrSc+=1
        print("Point goes to You")
    elif u.lower()=='s' and c=='r':
        compSc+=1
        print("Point goes to Computer")
    
    elif u.lower()=='p' and c=='p':
        print("Draw")
        draw+=1
    elif u.lower()=='p' and c=='r':
        usrSc+=1
        print("Point goes to You")
    elif u.lower()=='p' and c=='s':
        compSc+=1
        print("Point goes to Computer")

    print("\n")

print("\nTotal Scores ^_^\n")
print("User Score : ",usrSc)
print("Computer Score : ",compSc)
print("Draw : ",compSc)

if usrSc < compSc:
    print("Winner is Computer")
elif usrSc > compSc:
    print("Winner is You")
elif usrSc == compSc:
    print("Match Drawn")