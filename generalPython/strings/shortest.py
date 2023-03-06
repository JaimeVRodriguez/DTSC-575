import sys

sentence = str(sys.argv[1])

def shortest():
    short = None
    words = sentence.split()

    for word in words:
        if short == None:
            short = word.upper()
        elif len(word) < len(short):
            short = word.upper()
    
    print(f'The shortest word is {short}')

        

shortest()
