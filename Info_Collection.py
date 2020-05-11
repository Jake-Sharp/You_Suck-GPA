import GPA_Calc

classes= []
grades = []
clNum = 0
weightAdd = 0
weightAP = ' '
Local = False
       
    # Choice Betweem 4.0 and % systems
def algorithmChoice():
    global Local
    print("How are your Grades Measured?")
    print("1 - 4.0 System")
    print("2 - Percent Standard")
    print("3 - Go Back")
    print("4 - Quit")
    firstChoice = ' '
    while firstChoice != '1' or firstChoice !='2' or firstChoice != '3' or firstChoice !='4':
        firstChoice = input()
        if firstChoice == '1':
            print("4.0 System!")
            Local = True
            collectClass()
        elif firstChoice == '2':
            print("Percent Standard!")
            collectClass()
        elif firstChoice == '3':
            print("Going Back!")
            intro()
        elif firstChoice == '4':
            print("Goodbye!")
            break
            
   
    # Enter Grades 
def collectClass():
    
    print("How Many Classes do you Participate in?")
    print("1 - 1")
    print("2 - 2")
    print("3 - 3")
    print("4 - 4")
    print("5 - 5")
    print("6 - 6")
    print("7 - 7")
    print("8 - 8")
    print("9 - Go Back")
    #print("Q - Quit")
    cNum = ' '
    while cNum != '1' or cNum !='2' or cNum !='3' or cNum != '4' or cNum !='5' or cNum !='6' or cNum != '7' or cNum !='8' or cNum !='9':
        cNum = input()
        if cNum == '9':
            print("Going Back!")
            algorithmChoice()
        elif cNum == 'Q':
            print("Goodbye!")
            break
        
        for i in range(int(cNum)):
            className = input("Enter Class Name: ")
            classes.append(className)
        
        for j in range(int(cNum)):
            if Local == True:
                grade = input("Enter your Grade: ")
                grade = grade.upper()
                grades.append(grade)
    
            elif Local == False:
                grade = int(input("Enter your Grade: "))
                grades.append(grade)
        weight()
        
def weight():
    print("Do you Partcipate in any AP Classes?")
    print("1 - Yes")
    print("2 - No")
    print("3 - Go Back")
    print("4 - Quit")
    APchoice = ' '
    while APchoice != '1' or APchoice !='2' or APchoice != '3' or APchoice !='4':
        APchoice = input()
        if APchoice == '1':
            weightAP = int(input("How many AP Classes do you participate in?: "))
            if Local == True:
                weightAdd = weightAP
                GPA_Calc.fourpoint()
            elif Local == False:
                weightAdd = (10) * (weightAP)
                GPA_Calc.percent() 
        elif APchoice == '2':
            print("Let's Continue")
            if Local == True:
                GPA_Calc.fourpoint()
            elif Local == False:
                GPA_Calc.percent() 
        elif APchoice == '3':
            print("Going Back!")
            collectClass()
        elif APchoice == '4':
            print("Goodbye!")
            break
