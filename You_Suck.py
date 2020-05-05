import Info_Collection
import time

# Intro
def intro():
    print("Welcome to reality Loser")
    print("Would you like to Continue? (Y/N)")
    Continue = ' '
    while Continue != 'Y' or Continue !='N':
        Continue = input()
        if Continue == 'Y':
            print("What a waste of my time!")
            Info_Collection.algorithmChoice()
        elif Continue == 'N':
            print("FUCKING LOSER!")
            print("NOBODY LOVES YOU!")
            break
        elif Continue != 'Y' or Continue != 'N':
            intro()
    
     
intro()
