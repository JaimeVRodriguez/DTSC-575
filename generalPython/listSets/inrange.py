import sys

num = int(sys.argv[1])

def divisible():
    arg1 = num
    arg2 = num + 7
    arg3 = num ** 2
    div = []

    for i in range(3000, 5001):
        if (i % arg1 == 0) and (i % arg2 == 0) and (i % arg3 == 0):
            div.append(i)
        
    print(div)
        

divisible()