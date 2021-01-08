while True:
    try:
        dna = input()
        resist = input()
        if resist in dna:
            print('Resistente')
        else:
            print('Nao resistente')
    except EOFError:
        break
