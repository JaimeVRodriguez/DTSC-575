
import sys

item = str(sys.argv[1])

def averageScore():
    grades = {'Biology':80, 'Physics':88, 'Chemistry':98, 'Math':89, 'English':79, 'Music':67, 'History':68, 'Art':53, 'Economics':95, 'Psychology':88}

    del grades[item]
    
    total = 0
    for value in grades.values():
        total += value

    avg = total / len(grades)
    print(round(avg, 2))

averageScore()