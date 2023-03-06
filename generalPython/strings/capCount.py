import sys

sentence = str(sys.argv[1])

def capCount():
    num_caps = 0
    for letter in sentence:
        if letter.isupper():
            num_caps += 1

    print(num_caps)

    index_sum = 0
    for i, c in enumerate(sentence):
        if c.isupper():
            index_sum += i
    print(index_sum)

capCount()