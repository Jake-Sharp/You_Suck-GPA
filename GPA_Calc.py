import Info_Collection
#from Info_Collection import grades

def fourpoint():
    print("4.0")
    total = 0
    i = 0
    for i in Info_Collection.grades:
        if i == "A+":
            total = total + 4.0
        elif i == "A":
            total = total + 4.0
        elif i == "A-":
            total = total + 3.7
        elif i == "B+":
            total = total + 3.3
        elif i == "B":
            total = total + 3.0
        elif i == "B-":
            total = total + 2.7
        elif i == "C+":
            total = total + 2.3
        elif i == "C":
            total = total + 2.0
        elif i == "C-":
            total = total + 1.7
        elif i == "D":
            total = total + 1.0
    GPA = total / 6
    respond()
    
def percent():
    print("%")
    Total = 0
    i = 0
    for i in Info_Collection.grades:
        total = total + float(grades[i])
        i = i + 1
    gpa = Total / 6

def respond():
    if Info_Collection.Local == True:
        print(GPA)
    elif Info_Collection.SLocal == False:
        print(gpa)
    
