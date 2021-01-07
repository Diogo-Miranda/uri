import math
while True:
    try:
        num = float(input())
        cutoff = float(input())
        frac = num - int(num)
        if frac > cutoff:
            print(math.ceil(num))
        else:
            print(int(num))
    except EOFError:
        break
