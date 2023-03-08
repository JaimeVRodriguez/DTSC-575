import pandas as pd
import sys

x = int(sys.argv[1])
y = int(sys.argv[2])

def avgHeight():
    df = pd.read_csv('president_heights.csv')
    heightSum = 0
    heights = df[x:y]['height(cm)']

    for height in heights:
        heightSum += height

    z = heightSum / len(heights)

    print(f'The average height of presidents number {x} to {y} is {z:.2f}')

avgHeight()
