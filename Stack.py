# Class Stack
class Stack:
    def __init__(self):
        self.stack=[]

    def push(self, val):
        self.stack.append(val)

    def isempty(self):
        return len(self.stack)==0

    def pop(self):
        if self.isempty():
            print("Stack is Empty")
            return
        return self.stack.pop()

    def peek(self):
        if not(self.isempty()):
            return self.stack[-1]

    def display(self):
        for x in self.stack:
            print(x," ")

    def size(self):
        return len(self.stack)

My=Stack()

My.push('D')
My.push('S')
My.push('A')

print(My.peek())
print(My.size())
print(My.isempty())
print(My.display())

