numTests = int(input())

for i in range(numTests):
    numStudents = int(input())
    if numStudents > 0:
        nameStudents = input().split(' ')
        frequency = input().replace('M', '').split(' ')

        failed = []
        for index, score in enumerate(frequency):
            fail = score.count('A')
            total = len(score)
            isReproved = False if 100 - (100*fail)/total >= 75 else True
            if isReproved:
                failed.append(nameStudents[index])
        print(' '.join(failed))
    else:
        print()
