
def rev(L, start, fin):
    cur = L
    
    for i in range(start - 2):
        cur = cur.next

    prv, cur, nxt = cur, cur.next, cur.next.next

    for i in range(fin - start):
        # nxt = cur.next.next or None
        cur.next = prv
        prv, cur, nxt = cur, nxt, nxt.next
    
    
        
        
        
        
    
    
    
