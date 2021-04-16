# Implement the Stack class from scratch (do not use your language’s standard stack or queue library/package methods).
#  In this challenge, your Stack will only accept Integer values. 
# Implement the following methods:
#push() → Pushes an integer on top of the stack
#pop() → Removes what is on the top of the stack, and returns that value to the caller
#top() → Looks at the top value, and returns it. Does not manipulate the stack
#isEmpty() → Returns True or False if the stack is Empty or not, respectively
#size() → Returns an integer value with the count of elements in the stack

#define class
class Stack():
    #Constructor
    def __init__(self):
        self.slist = []

    def push(self, item):
        self.sList.append(item)

    def pop(self):
        return self.sList.pop()

    def top(self):
        return self.sList[-1]

    def isEmpty(self):
        return len(self.sList) == 0

    def size(self):
        return len(self.sList)

#Implement a Queue class from scratch that handles integers, with the following methods: 
#enqueue() → adds an item to the queue
#dequeue() → removes an item from the queue
#rear() → returns the item at the end of the queue
#front() → returns the item at the front of the queue
#size() → returns the size of the queue
#isEmpty() → returns whether or not the queue is empty
class Queue():
    def __init__(self):
        self.qList = []

    def enqueue(self,item):
        self.qList.insert(0,item)

    def dequeue(self):
        self.qList.pop()

    def rear(self):
        return self.qList[-1]

    def size(self):
        return len(self.qList)

    def isEmpty(self):
        return len(self.qList) == 0


