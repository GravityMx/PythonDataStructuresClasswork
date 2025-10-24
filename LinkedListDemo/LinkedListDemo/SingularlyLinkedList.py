
class Node:
    
    def __init__(self, value, next=None):
        self.Value = value
        self.Next = next


class Stack:
    # Same as the infix and postfix program
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


class SinglyLinkedList:
    
    def __init__(self):
        self.Head = None
        self._Count = 0


    # Basic helpers / queries


    def IsEmpty(self):
        return self.Head is None

    def Length(self):
        return self._Count

    def Clear(self):
        self.Head = None
        self._Count = 0

    
    # Insertion
    def InsertAtFront(self, value):
        node = Node(value, self.Head)
        self.Head = node
        self._Count += 1

    def InsertAtEnd(self, value):
        node = Node(value, None)
        if self.Head is None:
            self.Head = node
            self._Count += 1
            return
        cur = self.Head
        while cur.Next is not None:
            cur = cur.Next
        cur.Next = node
        self._Count += 1

    # building list forward
    # That’s equivalent to InsertAtEnd for each value.
    def BuildListForward(self, values):
        for v in values:
            self.InsertAtEnd(v)




    # Delete
    def DeleteFirst(self):
        if self.Head is None:
            return None
        val = self.Head.Value
        self.Head = self.Head.Next
        self._Count -= 1
        return val

    def DeleteLast(self):
        if self.Head is None:
            return None
        if self.Head.Next is None:
            val = self.Head.Value
            self.Head = None
            self._Count -= 1
            return val

        prev = None
        cur = self.Head
        while cur.Next is not None:
            prev = cur
            cur = cur.Next
        # cur is last, prev is node before last
        prev.Next = None
        self._Count -= 1
        return cur.Value

    # delete by index (0-based) to make “interior delete” explicit
    def DeleteAtIndex(self, index):
        if index < 0 or index >= self._Count or self.Head is None:
            return None
        if index == 0:
            return self.DeleteFirst()

        prev = None
        cur = self.Head
        i = 0
        while i < index:
            prev = cur
            cur = cur.Next
            i += 1


        prev.Next = cur.Next
        self._Count -= 1
        return cur.Value

    


    # remove all
    def Remove_All(self, value):
        # sentinel to simmplify head-removals
        dummy = Node(0, self.Head)
        prev = dummy
        cur = self.Head
        removed = 0
        while cur is not None:
            if cur.Value == value:
                prev.Next = cur.Next
                removed += 1
                self._Count -= 1
            else:
                prev = cur
            cur = cur.Next
        self.Head = dummy.Next
        return removed


    def ToList(self):
        result = []
        cur = self.Head
        while cur is not None:
            result.append(cur.Value)
            cur = cur.Next
        return result



    def Display(self):
        # strings produce results like: "1 -> 2 -> 3"
        parts = []
        cur = self.Head
        while cur is not None:
            parts.append(str(cur.Value))
            cur = cur.Next
        return " -> ".join(parts) if parts else "(empty)"

    # display_reverse_nr() (just uses stack)
    def Display_Reverse_NR(self):
        st = Stack()
        cur = self.Head
        while cur is not None:
            st.Push(cur.Value)
            cur = cur.Next
        parts = []
        while st.Length() > 0:
            parts.append(str(st.Pop()))
        return " <- ".join(parts) if parts else "(empty)"











