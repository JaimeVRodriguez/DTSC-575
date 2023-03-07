import sys

set_a = sys.argv[1:]
set_b = ['apple', 'banana', 'mango', 'orange']

def common():
    common = set()
    for i in set_a:
        if i not in set_b:
            common.add(i)

    print(common)

common()