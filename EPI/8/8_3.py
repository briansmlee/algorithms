"""
8.3 parnethesis

0. T
well formed if diff types of brackets match in correct order
arg: string made up of chars (, {, [
ret: if well formed

1. C

2. EX
([]){()}

3. BF
4. Qs
- LIFO stack
last open must be closed first
if (,[,{ store in stack
if counterpart, pop.
if match, continue. else, ret false.

- corner or counterex?
nothing to pop. indexerror
opening parens left in stack after fin.

5. O
"""


