numStrs = int(input())
while numStrs != 0:
    strs = []
    for i in range(numStrs):
        strs.append(input())

    # find the bigger string
    largerStr = 0
    for string in strs:
        if len(string) > largerStr:
            largerStr = len(string)

    for string in strs:
        # justify
        print(f'{string:>{largerStr}}')

    numStrs = int(input())
    if numStrs != 0 : print()

