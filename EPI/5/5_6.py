"""
5.6 buy and sell a stock once

1. Task
arg: arr of daily stock prices
ret: max profit made by buy and sell one share of that stock

2. clarify
if no profit is possible? return 0

3. BF
all combinations of buy & sell dates
O(n^2) since n choose 2

Q: how to get max profit?
buy low and sell high

Q: why not lowest, highest?
highest before lowest.
buy before sell

Q: O(n lg n)?
div and conq
div L and R.
max profit is in L, R or buy in L and sell at R
if buy in L and sell at R, since buying before selling,
find lowest in L and highest in R.
O(N) each max min

Q: base?
if 1 elem, return 0

4. Outline
arg: A

helper function
arg: A, start, end

if start == end
return 0
mid
call on L and R
cur = max(A[mid:end + 1]) - min(A[start:mid]) 
return max(L, R, cur, 0)

O(n lg n)
"""

def buy_sell_once(A):
    
    def rec(A, start, end):
        if start == end:
            return 0
        if start + 1 == end:
            return max(A[end] - A[start], 0)
        mid = (start + end) // 2
        left_max = rec(A, start, mid - 1)
        right_max = rec(A, mid, end)
        cur_max = max(A[mid:(end + 1)]) - min(A[start:mid])
        return max(left_max, right_max, cur_max, 0)
    
    return rec(A, 0, len(A) - 1)


"""
Hint: O(n) solution exists
max profit is max among any profits made by selling on day.
given a day, consider all options to sell on that day.
among all those options, max profit if bought at lowest price.
then, O(1) per day, if we know lowest price so far.
so, keep track of lowest p so far, which is also O(1) per day.

Outline:
min_so_far = inf
max_so_far = 0

for days
cur_max = elem - min_so_far
max_so_far = max(cur_max, max_so_far)
min_so_far = min(price, min_so_far)

return max_so_far
"""

def buy_sell_once2(A):
    min_so_far = float('inf')
    max_so_far = 0
    
    for price in A:
        cur_max = price - min_so_far
        max_so_far = max(cur_max, max_so_far)
        min_so_far = min(price, min_so_far)
    
    return max_so_far

    
A = [310,315,275,295,260,270,290,230,255,250]
print(buy_sell_once(A))
print(buy_sell_once2(A))


