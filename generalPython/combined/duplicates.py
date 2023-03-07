import sys

duplicated_words = sys.argv[1:]

def dupes():
    single = [*set(duplicated_words)]
    single.sort(reverse=True)
    print(single)

dupes()