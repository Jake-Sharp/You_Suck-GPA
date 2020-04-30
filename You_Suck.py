
import time

Pass = False
GS1 = False
GS2 = False
c6 = False
c7 = False
c8 = False
a = 0

# Intro
def intro():
    print("WELCOME TO THE GPA CALCULATOR")
    choice1()
    
# Choice Betweem 4.0 and % systems
def choice1():
    global GS1, GS2
    print("(CHOOSE ALGORITHM)")
    print("1 - 4.0 System")
    print("2 - Percent Standard")
    firstChoice = ' '
    while firstChoice != '1' or firstChoice !='2':
        firstChoice = input()
        if firstChoice == '1':
            print("You Chose the 4.0 System!")
            GS1 = True
            classNum()
        if firstChoice == '2':
            print("You Chose Percent Standard!")
            GS2 = True
            classNum()
      

# Choose number of classes
def classNum():
    global c6, c7, c8
    print("How many classes do you have this semester?")
    print("1 - 6 Classes")
    print("2 - 7 Classes")
    print("3 - 8 Classes")
    secondChoice = ' '
    while secondChoice != '1' or secondChoice !='2' or secondChoice != '3':
        secondChoice = input()
        if secondChoice == '1':
            print("You Participate in 6 Classes!")
            c6 = True
            classSix()
            a = 6
        if secondChoice == '2':
            print("You Participate in 7 Classes!")
            c7 = True
            classSeven()
            a = 7
        if secondChoice == '3':
            print("You Participate in 8 Classes!")
            c8 = True
            classEight()
            a = 8

        
# Enter Grades 6
def classSix(len(a)):
    global c6
    cls6 = []
    print("6 Working")
    print("Enter Your Grades: ")
    print("(A+, A, A-, etc)")

# Enter Grades 7
def classSeven(len(a)):
    global c7
    cls7 = []
    print("7 Working")
    print("Enter Your Grades: ")
    print("(A+, A, A-, etc)")

# Enter Grades 8
def classEight(len(a)):
    global c8
    cls8 = []
    print("8 Working")
    print("Enter Your Grades: ")
    print("(A+, A, A-, etc)")

# 4.0 System
def fourPoint():
    global c6, c7, c8
    print("4.0 Working")

# Percent Standard
def percentStandard():
    global c6, c7, c8
    print("Percent Standard Working")


intro()
