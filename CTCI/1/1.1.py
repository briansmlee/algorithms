# CTCI 1.1
# determine if a string has all unique characters.

# assumption for the code below is wrong:
# by "having all unqiue characters",
# not asking if a string as all ASCII chars
# but if all chars in str are unique.

# using additional data structure
# def is_unique(A):
#     arr = [0] * 128
#    
#     for c in A:
#        arr[ord(c)] += 1
#     
#     for a in arr:
#         if a == 0:
#             return False
# 
#     return True
# 
# A = 'abcde'
# print(is_unique(A)) # print false
# 

# with new assumptions
# O(n)
def is_unique(A):
    count = [False] * 128
    for c in A:
        if count[ord(c)] == True:
            return False
        else:
            count[ord(c)] = True
    return True
        
# w/o additional DS
# O(n log n) by sorting
def is_unique1(A):
    A.sort()
    for i in range(len(A) - 1):
        if A[i] == A[i + 1]:
            return False
    return True

"""
Note:
0. ASCII is 128, extended ASCII is 256
1. if len of str exists num of possible chars, by pigeonhole, not unique.
2. space complexity is O(1).
3. could argue that time complexity is O(1), since loop no longer than 128 
*** 4. if char set is not fixed, then time is O(min(c, n)),
    where c is size of char set, n is len of array,
    since max number of loops is min(c, n).
*** 5. use bit vector
*** 6. SORTING ALGORITHM MAY TAKE ADDITIONAL SPACE!!! must use in-place sort
"""
        
        
