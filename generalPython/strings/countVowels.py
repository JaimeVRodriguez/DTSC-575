import sys

word = str(sys.argv[1])

def countVowels():
    vowels = ['a', 'e', 'i', 'o', 'u']
    newWord = word.lower()
    vowelCount = {}
    for letter in newWord:
        if letter in vowels:
            if letter in vowelCount:
                vowelCount[letter] += 1
            else:
                vowelCount[letter] = 1

    print(len(vowelCount))

countVowels()



