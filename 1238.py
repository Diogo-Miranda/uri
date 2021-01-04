numTests = int(input())
for i in range(numTests):
    str1, str2 = input().split(' ')
    newStr = ''
    # check which string is greater
    greaterLen = 0
    if len(str1) > len(str2):
        greaterLen = len(str1)
    else:
        greaterLen = len(str2)

    # concat strings
    for index in range(greaterLen):
        if index < len(str1):
            newStr += str1[index]
        if index < len(str2):
            newStr += str2[index]

    print(newStr)
