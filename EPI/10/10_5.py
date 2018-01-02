"""
10-5 median of online data

0. T
running med of seq of nums
stream
MODIFY: if query, output median

1. EX

2. C
- odd?
len(A) // 2 + 1
- even?
smaller

3. BF
keep all.
sort every query.

4. Qs
heap
- min. keeping larger half
- sz?
len // 2 + 1? NO!!!
size must increase.
1 1
2 1
3 2
4 2
5 3 
6 3

- bit
keep a bit,
if 0, just push
if 1, push then pop

- if min < new, replace.

- query?
ret h[0]

- if doing check, size not inc.
since we're keeping more items, should not check with min.
however, unsure if new item is one below the min!

- two heaps?
lower half is max heap, higher half is min heap.

- sz?
same if even
higher half has one more if odd,
since return fst of higher.

- insert()?
compare with both. know which half.
insert to that half.
balance size

- easier?
always insert to higher half.
if sps to be in lower half, will be min.
always pop from higher and insert to lower half.

- balance?
if lower has more, move to higher.

- pop anything?
no.

- median()
ret min of higher.

5. Edge
- fst?
push to higher.

- snd

6. Out

7. TS
n lg(n / 2)
"""

