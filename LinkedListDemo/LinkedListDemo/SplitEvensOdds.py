
from SinglyLinkedList import SinglyLinkedList

class SplitEvensOdds(SinglyLinkedList):


    def SplitIntoEvensOdds(self):
        evens = SinglyLinkedList()
        odds  = SinglyLinkedList()


        evenTail = None
        oddTail  = None

        cur = self.Head
        while cur is not None:
            nxt = cur.Next       # save next before we detach
            cur.Next = None      # detach this node from old chain 



            v = cur.Value
            isEven = (isinstance(v, int) and (v % 2 == 0))

            if isEven:
                if evens.Head is None:
                    evens.Head = cur
                    evenTail = cur
                else:
                    evenTail.Next = cur
                    evenTail = cur
                evens._Count += 1

            else:
                if odds.Head is None:
                    odds.Head = cur
                    oddTail = cur
                else:
                    oddTail.Next = cur
                    oddTail = cur
                odds._Count += 1

            cur = nxt

        # Original list becomes empty
        self.Head = None
        self._Count = 0

        return evens, odds



