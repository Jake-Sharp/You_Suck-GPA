import Info_Collection
import time

# Intro
def intro():
    print("Welcome to your GPA Calculator")
    print("Would you like to Continue?")
    print("1 - Yes")
    print("2 - No")
    print("3 - Quit")
    Continue = ' '
    while Continue != '1' or Continue !='2' or Continue !='3':
        Continue = input()
        if Continue == '1':
            print("Let's Continue!")
            Info_Collection.algorithmChoice()
        elif Continue == '2':
            print("Restart")
            intro()
        elif Continue == '3':
            print("Goodbye!")
            break
    
     
intro()
