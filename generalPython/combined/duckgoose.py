import sys

duck_goose = sys.argv[1:]

def duckGoose():
    ducks = []
    for i in duck_goose:
        if i != 'goose':
            ducks.append(i)

    print(ducks)

duckGoose()