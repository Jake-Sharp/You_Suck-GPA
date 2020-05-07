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
    print("Your GPA is: " + str(GPA))
    
def percent():
    Total = 0
    for i in Info_Collection.grades:
        Total += Info_Collection.grades([i])
        
    gpa = Total / len(Info_Collection.classes)
    print("Your GPA is: " + str(gpa) + " %")
    
