
GPA = ' '
gpa = 0
def fourpoint():
    print("4.0")
    
    def calculate():
    total= 0
    for element in grades:
        if element == "A+":
            total = total + 4.0
        elif element == "A":
            total = total + 4.0
        elif element == "A-":
            total = total + 3.7
        elif element == "B+":
            total = total + 3.3
        elif element == "B":
            total = total + 3.0
        elif element == "B-":
            total = total + 2.7
        elif element == "C+":
            total = total + 2.3
        elif element == "C":
            total = total + 2.0
        elif element == "C-":
            total = total + 1.7
        elif element == "D":
            total = total + 1.0
    GPA = total / 6
    respond()
    
def percent():
    print("%")
    
    def calculate():
    total= 0
    for element in grades:
        if element == "A+":
            total = total + 4.0
        elif element == "A":
            total = total + 4.0
        elif element == "A-":
            total = total + 3.7
        elif element == "B+":
            total = total + 3.3
        elif element == "B":
            total = total + 3.0
        elif element == "B-":
            total = total + 2.7
        elif element == "C+":
            total = total + 2.3
        elif element == "C":
            total = total + 2.0
        elif element == "C-":
            total = total + 1.7
        elif element == "D":
            total = total + 1.0
    gpa = total / 6
    respond()

def respond():
    print(GPA)
