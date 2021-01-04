while True:
    try:
        string = input().lower()
        newString = ''
        isUpperCase = 0  # this flag verify if the actual letter is upper case
        for letter in string:
            # verify if the current letter is a 'space'
            if letter != ' ':
                # if the current letter isn't upper case
                if isUpperCase == 0:
                    newString += letter.upper()
                    isUpperCase = 1
                else:
                    newString += letter
                    isUpperCase = 0
            else:
                newString += letter

        print(f'{newString}')
    except EOFError:
        break
