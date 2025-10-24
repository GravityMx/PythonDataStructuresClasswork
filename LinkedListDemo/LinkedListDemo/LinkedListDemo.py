
from SinglyLinkedList import SinglyLinkedList

from SplitEvensOdds import SplitEvensOdds

def PrintList(label, list):
    print(label, " = ", list.Display())

def PrintListRev(label, list):
    print(label, " = ", list.Display_Reverse_NR())

test = SinglyLinkedList()
    
test.BuildListForward([1, 2, 3, 4, 5])
    
PrintList("Forward build", test)


    
test.DeleteFirst()
PrintList("After DeleteFirst", test)

test.DeleteLast()
PrintList("After DeleteLast", test)




test.DeleteAtIndex(1)
PrintList("After DeleteAtIndex(1)", test)

PrintListRev("Reverse (NR)", test)

test.InsertAtEnd(2)
test.InsertAtEnd(2)
PrintList("Before Remove_All(2)", test)
removed = test.Remove_All(2)
print("Removed count = ", removed)
PrintList("After Remove_All(2)", test)


print("Split test: BuildListForward")
s = SplitEvensOdds()
s.BuildListForward([1, 2, 3, 4, 5, 6, 7, 8])
PrintList("Starter List", s)

evens, odds = s.SplitIntoEvensOdds()
PrintList("Evens", evens)
PrintList("Odds", odds)
PrintList("Original (should be empty)", s)



print("Split test: InsertAtEnd")
s2 = SplitEvensOdds()
for x in [10, 11, 12, 13, 14]:
    s2.InsertAtEnd(x)
PrintList("Starting list", s2)


ev2, od2 = s2.SplitIntoEvensOdds()
PrintList("Evens", ev2)
PrintList("Odds", od2)
PrintList("Original", s2)








