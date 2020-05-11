import Info_Collection


GPA = 0.0
gpa = 0.0

def fourpoint():
    total = 0
    for i in Info_Collection.grades:
        if i == "A+":
            total += 4.3
        elif i == "A":
            total += 4.0
        elif i == "A-":
            total += 3.7
        elif i == "B+":
            total += 3.3
        elif i == "B":
            total += 3.0
        elif i == "B-":
            total += 2.7
        elif i == "C+":
            total += 2.3
        elif i == "C":
            total += 2.0
        elif i == "C-":
            total += 1.7
        elif i == "D+":
            total += 1.3
        elif i == "D":
            total += 1.0
        elif i == "D-":
            total += 0.7

    GPA = total / len(Info_Collection.classes)
    respond()
    
def percent():
    Total = sum(Info_Collection.grades)
    gpa = Total / len(Info_Collection.classes)
    respond()

def respond(): #Scratch this and return both without the question tomorrow
    print("Would you Like to see your Weighted or Unweighted GPA?")
    print("1 - Weighted")
    print("2 - Unweighted")
    print("3 - Go Back")
    print("4 - Quit")
    resChoice = ' '
    while resChoice != '1' or resChoice !='2' or resChoice != '3' or resChoice !='4':
        resChoice = input()
        if resChoice == '1':
            if Info_Collection.Local == True:
                print("Your GPA is: " + str(GPA + Info_Collection.weightAdd))
            if Info_Collection.Local == False:
                print("Your GPA is: " + str(gpa + Info_Collection.weightAdd) + " %")
        elif resChoice == '2':
            if Info_Collection.Local == True:
                print("Your GPA is: " + str(GPA))
            if Info_Collection.Local == False:
                print("Your GPA is: " + str(gpa) + " %")
        elif resChoice == '3':
            print("Going Back!")
            weight()
        elif resChoice == '4':
            print("Goodbye!")
            break

    
    
