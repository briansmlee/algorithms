

# palindrome

def f(s):
    i, j = 0, len(s) - 1
    while i < j:
        if not s[i].isalnum():
            i += 1
            continue
        if not s[j].isalnum():
            j -= 1
            continue

        # both are alnum
        if s[i].lower() != s[j].lower():
            return False
       
        i += 1
        j -= 1

    return True

s = 'A man, a plan, a canal, Panama.'
print(f(s))
s1 = 'Ray a Ray'
print(f(s1))

