import sys

character = str(sys.argv[1])

def relationship():
    relations = {'Darth Vader':'father', 'Leia':'sister', 'Han':'brother in law', 'R2D2':'droid', 'Rey':'Padawan', 'Tatooine':'homeworld'}


    if character == 'Darth Vader':
        print('No, I am your father')
    else:
        print(f'Luke, I am your {relations[character]}')

relationship()