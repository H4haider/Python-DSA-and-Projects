# Class Queue

class Queue:
    def __init__(self):
        self.queue=[]

    def enqueue(self, val):
        self.queue.append(val)

    def dequeue(self):
        return self.queue.pop(0)

    def peek(self):
        return self.queue[0]

    def size(self):
        return len(self.queue)

    def isempty(self):
        return len(self.queue)==0

    def display(self):
        for x in self.queue:
            print(x, " ")

MyQueue=Queue()

MyQueue.enqueue('D')
MyQueue.enqueue('S')
MyQueue.enqueue('A')

print("Queue: ")
MyQueue.display()
print("Size: ", MyQueue.size())
