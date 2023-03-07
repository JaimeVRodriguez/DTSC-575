import sys

my_ints = sys.argv[1:]

def convert():
    ints = []
    for i in my_ints:
        num = int(i)
        if num % 3 == 0:
            ints.append(num*10)
        else:
            ints.append(num)

    print(ints)

convert()