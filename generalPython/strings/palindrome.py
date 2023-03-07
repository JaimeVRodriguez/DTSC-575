import sys

phrase = str(sys.argv[1])
def palindrome():
    aString = ''

    for i in phrase:
        if i.isalpha() or i.isdigit():
            aString += i.lower()

    if aString == aString[::-1]:
        print('It\'s a palindrome!')
    else:
        print('It\'s not a palindrome!')

palindrome()
