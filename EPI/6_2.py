import string

def convert_base(s, b1, b2):
    n = len(s)
    num = 0
    
    for i in reversed(range(n)):
        num += (b1**i) * int(s[n - 1 - i])

    print(num)

    quot, rem, res = num, 0, []
    while quot:
        rem = quot % b2
        quot = quot // b2
        res.append((str(rem) if rem < 10 else chr(ord('A') + (rem - 10))))
    
    return str(list(reversed(res)))

s = '615'
b1 = 7
b2 = 13
print(convert_base(s, b1, b2))
        
        
        
