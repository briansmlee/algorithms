
def max_p(A):
    """ 
    
    obs: index-wise buy < sell
    div conq: max buy, sell either in L, R, both;
    -> always catch end cases!!!
    if both, how to find max?
    obs: max = sell lowest buy highest
    """
    if len(A) == 1:
        return 0 
    mid = len(A) // 2
    adj = max(A[mid:]) - min(A[0:mid]) 

    return max(max_p(A[0 : mid]), max_p(A[mid:]), adj, 0)

def max_p1(A):
    """
    
    pf: must buy, sell at t1, t2
    if sell at t2, buy at min price of all prev days
    consider all combs of t2 and min price: O(n)
    """
    min_price, max_profit = float('inf'), 0.0
    for price in A:
        min_price = min(min_price, price)
        prof = price - min_price
        max_profit = max(prof, max_profit)
    return max_profit

A = [310,315,275,295,260,270,290,230,255,250]
print(max_p1(A))
