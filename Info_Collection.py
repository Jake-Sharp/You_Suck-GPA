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
            print("Ew really? where are you from? Wisconsin?")
        classAttend()
            
    # Enter Number of Classes
def classAttend():
    cNum = input("How Many lousy Classes do you Participate in?")
    print("Only " +(cNum)+ " Classes? You need to ACTUALLY Try you lazy brat!")
    collect()


    # Enter Grades 
def collect():
    i = 0
    while (i <= cNum):
        className = input("Enter Class Name: ")
        classes.append(className)
        i = i +1

    y = 0
    while (y <= cNum):
        grade = input("Enter Your Grade For Each Class Listed in Order (Letter Form): ")
        grade = grade.upper()
        grades.append(grade)
        y = y + 1

def algType():
    if Local == True:
        GPA_Calc.fourpoint()
    elif Local == False:
        GPA_Calc.percent()



