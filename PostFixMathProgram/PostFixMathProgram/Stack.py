

class Stack:
    
    def __init__(self):
        self.list = []

    def Push(self, item):
        self.list.append(item)

    def Pop(self):
        return self.list.pop()

    def Peek(self):
        if not self.list:
            return None
        return self.list[-1]

    def Length(self):
        return len(self.list)