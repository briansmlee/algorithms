"""
CTCI 1.9 String Rotation

Task:
- sps you have isSubstring(s1, s2).
- given s1, s2, check if s2 is a rotation of s1,
- using only one call to isSubstring

Q: def of rotation?
- there exists a partiton of s1, s2,
- such that partitions match.
- more specifically, order of two is flipped

Q: how is that rel to isSub?
- if both parts are substring of s2? not iff.
- no need to check all partitions!
    since s2 has starting char, gives us a substring in s1
    that is, start of s2 in s1 to end of s1.
    but can be multiple same chars.
- if 1st of s1 is substring of s2, then only two options exist:
    1st|2nd or 2nd|1st. check if either matches s2 exactly.

Q: what if multiple same chars?
- must check all

back to two Qs:
1. what are two input strs to isSub?
2. what to do after?

Q: what if concat s2 twice? call is S.
- if s2 is rot of s1, then s1 is substring of S

Q: if s1 is substr of S, then s2 is rot of s1?
- if s1 is substr of S = A|BA|B,
    then s1 == BA.
    then A and B at end and start is determined.
    so, yes, s2 is rot of s1.

Outline:
- cocnat
- s1 isSub of concat
- ret T if T
"""

def is_rot(s1, s2):
    concat = s2 * 2
    return isSubstring(s1, concat)
    
    

