"""
3.2 Stack Min

Task:
- implement stack which returns minimum element.
- push, pop, min should be O(1)

Q: BF?
- search for min in stack every call. O(N)

Q: how to O(1)?
- this means in every call to min(), we "know" the min?
- invariant: maintain min in every push/pop

Q: how to keep min in push/pop?
push:
- compare cur min with new elem, replace if cur is smaller.
- O(1)
pop:
- either min is popped or not.
- if min is popped, need to know next min.
- by only keeping one min, impossible.
- since stack is LIFO, pops happen in order.
- if we keep min-so-far for every elem in stack,
  that info is always true!

Q: how to keep min-so-far for every elem?
push:
- compare min-so-far of top with new elem.
- take smaller, and keep in min-so-far of new elem.
- O(1)

pop:
- same!
- O(1)

min:
- return min-so-far of top.
- O(1)
"""

class MinStack():
    stack = []
    
    def push(self, elem):
        min_so_far = elem if not self.stack else min(elem, self.stack[-1][1])
        self.stack.append((elem, min_so_far))
        
    def pop(self):
        return self.stack.pop()[0]

    def min(self):
        return self.stack[-1][1]

stack = MinStack()
for i in range(5):
    stack.push(i)
print(stack.pop())
print(stack.min())


