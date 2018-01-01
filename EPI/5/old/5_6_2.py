
# brute force O(n^2)
# div and conquer?
# correctness:
# buy and sell in both L,R, or each in L, R
# same instance of problem

def buysell(A):
    if len(A) == 1:
        return 0
        
    mid = len(A) // 2 + 1
    return max(
        buysell(A[:mid]), 
        buysell(A[mid:-1]), 
        max(A[mid:-1]) - min(A[:mid]),
        0)


# min_price, max_profit
# think loop invariant

def buysell2(A):
    cur_max, cur_min = 0, float('inf')
    for i in range(len(A)):
        cur_min = min(cur_min, A[i])
        cur_max = max(cur_max, A[i] - cur_min)
    return cur_max

A = [310,315,275,295,260,270,290,230,255,250]
print(buysell2(A))


