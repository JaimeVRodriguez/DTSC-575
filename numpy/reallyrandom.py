import numpy as np
import sys

seed = np.random.seed(42)

size = int(sys.argv[1])
multiplier = int(sys.argv[2])
index = int(sys.argv[3])

def random_val():
    arr = np.random.randint(0, 10, size=size)
    arr2 = arr * multiplier
    if index < size:
        val = arr2[index]
        print(f'Your random value is {val}')
    else:
        None


random_val()