"""
CTCI 3.3 Stack of plates

Task:
- implement DS s.t. start a new stack when prev exceeds threshold.

Q: any pitfalls?
- keep track of which stack is self.top

Outline:
push:
- if full after push, change next to new stack.
pop:
- if empty prior to pop, change to old stack.
"""

class SetOfStacks():
    stacks = [[]]
    top = 0 # index of self.top stack
    cap = 2
    
    def push(self, elem):
        self.stacks[self.top].append(elem)
        if len(self.stacks[self.top]) == self.cap:
            self.stacks.append([])
            self.top += 1

    def pop(self):
        if len(self.stacks[self.top]) == 0:
            self.stacks.pop()
            self.top -= 1
        return self.stacks[self.top].pop()
    
    def show(self):
        print(self.stacks)

s = SetOfStacks()
for i in range(5):
    s.push(i)
print(s.pop())
s.show()

