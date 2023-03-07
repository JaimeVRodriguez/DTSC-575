import numpy as np
import sys

num1 = int(sys.argv[1])
num2 = int(sys.argv[2])
num3 = int(sys.argv[3])
num4 = int(sys.argv[4])

def npArray():
    nums = [num1, num2, num3, num4]
    arr = np.array(nums)

    print(type(arr))
    print(np.prod(arr))

npArray()