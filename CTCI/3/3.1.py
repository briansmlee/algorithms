"""
3.1 Three stacks in one

Task:
describe how to use single array to implement three stacks.

Q: two stacks?
- base at both ends.

Q: start a third stack from top of another?
- have to move elems in third stack every push to the one below.

Hint: circular array?

Ans:
- solution code for this problem is very long.
- partition array into 3 equal spaces,
  and resize when one is full,
  by wrapping around the third into the first.
"""


