#Choice Betweem 4.0 and % systems
def choice():
    print("CHOOSE ALGORITHM")
    print("1 - 4.0 System")
    print("2 - Percent Standard")
    firstChoice = ' '
    while firstChoice != '1' or firstChoice !='2':
        firstChoice = input()
        if firstChoice == '1':
            print("You Chose the 4.0 System")
            fourPoint()
        if firstChoice == '2':
            print("You chose Percent Standard")
            percent()

#4.0 System Input
def fourPoint():
    #ask for numer of classes
    #ask for grade input

    algOne() #4.0 Equation

#Percent Standard Input
def percent():
    #ask for numer of classes
    #ask for grade input
    
    algTwo() #Percent Equation

def algOne():
    #I'll research this tomorrow
    
def algTwo():
    #I'll research this tomorrow
