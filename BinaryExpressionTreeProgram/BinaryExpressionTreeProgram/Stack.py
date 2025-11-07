

class Stack:
    
    def __init__(self):
        self.list = []

    def push(self, item):
        self.list.append(item)

    def pop(self):
        return self.list.pop()

    def peek(self):
        if not self.list:
            return None
        return self.list[-1]

    def length(self):
        return len(self.list)

    def is_empty(self):
        return (self.length == 0)


