import GPA_Calc

classes= []
grades = []
cNum = 0
Local = False

       
    # Choice Betweem 4.0 and % systems
def algorithmChoice():
    global Local
    print("How are your Grades Measured?")
    print("1 - 4.0 System")
    print("2 - Percent Standard")
    firstChoice = ' '
    while firstChoice != '1' or firstChoice !='2':
        firstChoice = input()
        if firstChoice == '1':
            print("What a Normie")
            Local = True
        if firstChoice == '2':
            print("Ew really? Where are you from? Wisconsin?")
        classAttend()
            
    # Enter Number of Classes
def classAttend():
    cNum = int(input("How Many lousy Classes do you Participate in?"))
    print("Only " +(str(cNum))+ " Classes? You need to ACTUALLY Try you lazy brat!")
    collectClass()


    # Enter Grades 
def collectClass():
    i = 0
    print("Let's Collect Your Info")
    for i in range(cNum):
        className = input("Enter Class Name: ")
        classes.append(className)
        i = i + 1
    j = 0
    for j in range(cNum):
        if Local == True:
            grade = input("Enter Your Grade For Each Class Listed in Order (Letter Form): ")
        elif Local == False:
            grade = input("Enter Your Grade For Each Class Listed in Order (2 Decimals): ")
        grade = grade.upper()
        grades.append(grade)
        j = j + 1
    algType()

    # Transfer Data
def algType():
    if Local == True:
        GPA_Calc.fourpoint()
    elif Local == False:
        GPA_Calc.percent()


        



