import sys

grade1 = str(sys.argv[1])
grade2 = str(sys.argv[2])
grade3 = str(sys.argv[3])
grade4 = str(sys.argv[4])

def calculator():
    gpa_dict = {'A':4.0, 'A-':3.66, 'B+':3.33, 'B':3.0, 'B-':2.66, 'C+':2.33, 'C':2.0, 'C-':1.66, 'D+':1.33, 'D':1.00, 'D-':.66, 'F':0.00}

    items = [grade1.upper(), grade2.upper(), grade3.upper(), grade4.upper()]
    
    total = 0

    for i in items:
        total += gpa_dict[i]

    gpa = total / 4

    print(f'My GPA is {gpa:.2f}')

calculator()