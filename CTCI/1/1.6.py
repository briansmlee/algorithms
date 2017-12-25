"""
CTCI 1.6 String Compression

Task:
- compress using counts of repeated chars
- a-z only
- if compressed >= original, return original

Q: brute force?
- iterate thru str and create list: ['a2', 'b1', ...], then join
- O(max(N, M)), where M is encoded str

Q: other ways to know if compressed >= original?
    Q: what is len of compressed?
    - 2 * distinct chars
- iff 2 * distinct char count >= original
- so, if DCC >= original len / 2, return original
    Q: odd?
    - use lower.
- O(N)

Q: faster ways?

TODO:
- init list A to join
- count of diff
- compute len(S) / 2
- iter S until diff char, keeping count
- add new encoding to A
- update count2
- if c >= o, return original

Q: last elem

""" 

def compress(S):
    A = []
    count = 0
    i = 0 
    limit = len(S) / 2

    while i < len(S):
        repeat = 1
        while i != len(S) - 1 and S[i] == S[i+1]:
            repeat += 1
            i += 1
        # diff character or end
        A.append(S[i] + str(repeat))
        repeat = 1
        i += 1
        count += 1
        if count >= limit:
            return S
    
    return ''.join(A)

S = 'aabcccccaaa'
print(compress(S))
    
