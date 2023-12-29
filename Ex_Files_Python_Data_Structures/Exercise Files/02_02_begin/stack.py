"""
Python Data Structures - A Game-Based Approach
Stack class
Robin Andrews - https://compucademy.net/
"""


class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0
        #return not self.items
    
    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()
    
    def peak(self):
        return self.items[-1]
    
    def size(self):
        return len(self.items)
    
    def __str__(self):
        return str(self.items)


if __name__ == "__main__":
    s = Stack()
    print(s)

    my_stack = Stack()
    my_stack.push(1)
    my_stack.push(2)
    my_stack.push(2)
    my_stack.pop()
    print(my_stack)
