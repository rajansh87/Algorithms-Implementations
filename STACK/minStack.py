class Stack:
    def __init__(self):
        self.min = None
        self.stack = list()
    # function to get minimum element of the stack
    def getMin(self):
        if len(self.stack) == 0:
            return -1
        else:
            return self.min
    # function to return the top element
    def top(self):
        if len(self.stack) == 0:
            return -1
        top = self.stack[-1]
        if self.min > top:
            return self.min
        else:
            return top
    # function to pop the element from the stack
    def pop(self):
        if len(self.stack) == 0:
            return
        top = self.stack[-1]
        self.stack.pop()
        if top < self.min:
            self.min = 2*self.min-top
    # function to append element in the array
    def push(self, item):
        if len(self.stack) == 0:
            self.min = item
            self.stack.append(item)
            return
        if item < self.min:
            self.stack.append(2*item - self.min)
            self.min = item
        else:
            self.stack.append(item)
