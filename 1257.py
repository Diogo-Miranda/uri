import string
alphabet = list(string.ascii_uppercase)

numTests = int(input())
for i in range(numTests):
    numStrings = int(input())
    finalHash = 0
    for j in range(numStrings):
        strIn = input()

        for index, letter in enumerate(strIn):
            posAlphabet = 0
            for indexAlphabet, letterAlphabet in enumerate(alphabet):
                if letter == letterAlphabet:
                    posAlphabet = indexAlphabet

            valueHashLetter = posAlphabet + j + index  # valueHash = (pos alphabet + numIn + pos element)
            finalHash += valueHashLetter
    print(finalHash)
