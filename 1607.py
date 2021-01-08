numTest = int(input())
for i in range(numTest):
    before, after = input().lower().split(" ")
    numChanges = 0
    for index, letter in enumerate(before):
        while letter != after[index]:
            if letter == 'z':
                letter = 'a'
            else:
                letter = chr(ord(letter) + 1)
            numChanges += 1
    print(numChanges)
