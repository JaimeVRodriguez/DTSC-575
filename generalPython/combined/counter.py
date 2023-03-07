import sys
phrase = sys.argv[1]

def counter():
    counts = {}
    for letter in phrase:
        if letter in counts:
            counts[letter] += 1
        else:
            counts[letter] = 1
    
    print(counts)

counter()