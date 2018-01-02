"""
6.5 Test Palindrome

Task
palindrome is string which when nonalphanum are removed,
reads same front and back, ignoring case.

1. C

2. EX
'A man, a plan, a canal, panama'

3. BF

4. Qs
reading front and back.

Q: rm nonalphanum?
ignore

Q: case?
tolower() both.

5. Out
let front, back be ptrs
while front < back:
if front is non-alphanum, front++, cont
if back ", back--, cont
if front.tolower() neq back.tolower() return false
front++, back--
ret T
"""

    

