"""
3.4 Queue via Stacks

Task
- implement queue using two stacks

Q: how to get first in item from queue?
- S is LIFO, Q is FIFO
- need to pull out bottom of stack
- only two stacks as DS. need to keep order of items

Outline
s1, s2
push
- push to s1
- O(1)
pop
- if not empty, pop from s2
- pop each in s1 and push to s2
- O(N)

Q: amortized O(1)?
"""

class MyQueue():
    s1, s2 = [], []

    def push(self, elem):
        self.s1.append(elem)

    def pop(self):
        if len(self.s2) == 0:
            while len(self.s1) != 0:
                tmp = self.s1.pop()
                self.s2.append(tmp)
        return self.s2.pop()

q = MyQueue()
for i in range(5):
    q.push(i)
print(q.pop())
