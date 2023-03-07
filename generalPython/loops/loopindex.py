import sys

loop_list = sys.argv[1:]

def indexCalc():
    addedList = []
    for idx, val in enumerate(loop_list):
        num = int(val)
        addedList.append(idx + num)
    print(addedList)

indexCalc()