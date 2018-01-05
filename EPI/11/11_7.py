"""
11-7

0.T
find min and max simultaneously
less than 2(n-1) comparisons

1.EX
[3,2,5,1,2,4]
1, 5

2.C
- distinct?

3.BF
2(n-1)

4.Qs
- sort, heap, ... etc won't work, since O(n)
- cmpr x with min. if x is min, don't compr with max.
not a guaranteed dec in runtime

- take pairs. cmpr smaller with the min, larger with the max.
3/2n cmprs.

5.Edge
6.Out
7.TS
