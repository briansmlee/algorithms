
def stoi(s):
    # lsd (r) to msd (l), char to int, add 10**n
    return functools.reduce(
            lambda cur, c: cur * 10 + string.digits[c],
            s[s[0] == '-':],
            0) * (-1 if s[0] == '-' else 1)

def itos(i):
    s = []
    is_neg = False
    if i < 0:
        is_neg = True

    while True:
        s.append(chr(ord('0')) + i % 10)
        i //= i // 10
        if i == 0:
            break
        



s = '-123'
print(stoi(s))

i = '-456'
print(itos(i))
