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
        collectClass()
            
   
    # Enter Grades 
def collectClass():
    
    cNum = int(input("How Many lousy Classes do you Participate in?"))
    print("Only " +(str(cNum))+ " Classes? You need to ACTUALLY Try you lazy brat!")
    print("Let's Collect Your Info")
    for i in range(cNum):
        className = input("Enter Class Name: ")
        classes.append(className)
        i += 1
    
    for j in range(cNum):
        if Local == True:
            grade = input("Enter Your Grade (Letter Form): ")
            grade = grade.upper()
            grades.append(grade)
        elif Local == False:
            grade = int(input("Enter Your Grade (2 Decimals): "))
            grades.append(grade)
            
        j += 1
    algType()

    # Transfer Data
def algType():
    if Local == True:
        GPA_Calc.fourpoint()
    elif Local == False:
        GPA_Calc.percent()


        



