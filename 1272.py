numTests = int(input())

for i in range(numTests):
    string = input().split(' ')
    newString = ''
    for word in string:
        if word != '':
            newString += word[0]
    print(newString)
