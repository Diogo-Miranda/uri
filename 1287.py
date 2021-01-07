while True:
    try:
        string = int(input().replace('l', '1').replace('O', '0').replace('o', '0').replace(',', '').replace(' ', ''))
        if string > 2147483647:
            print('error')
        else:
            print(string)
    except EOFError:
        break
    except ValueError:
        print('error')
