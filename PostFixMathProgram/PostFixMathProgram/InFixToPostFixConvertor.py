
from PostFixMathProgram.Stack import Stack

def InFixToPostFixConvertor(inFixStr):

   inFixList = inFixStr.split()

   flagDown = False
   flagIndex = None
   
   # First pass, go throught each character to find parenthesis

   for i, c in enumerate(inFixList):
       if c == "(":
           flagDown = True
           flagIndex = i
           break

   if flagDown:
       parenthesisCount = 0
       endIndex = None
       for i in range(flagIndex + 1, len(inFixList)):
           c = inFixList[i]
           if (c == "("):
               parenthesisCount += 1

           elif (c == ")"):
               if parenthesisCount <= 0:
                   endIndex = i
                   break
               else:
                   parenthesisCount -= 1

       orderedGroup = InFixToPostFixConvertor(' '.join(inFixList[flagIndex + 1 : endIndex]))
       inFixList[flagIndex : endIndex + 1] = [orderedGroup]  


   # Then go through each character to find * or / signs to swap

   i = 0
   while i < len(inFixList):
        c = inFixList[i]
        if c in ("*", "/"):
            lhs = inFixList[i - 1]
            rhs = inFixList[i + 1]
            merged = f"{lhs} {rhs} {c}"
            inFixList[i - 1 : i + 2] = [merged]
            i = max(0, i - 1)  
        else:
            i += 1

   # Then go through each character to find + or - signs to swap

   i = 0
   while i < len(inFixList):
        c = inFixList[i]
        if c in ("-", "+"):
            lhs = inFixList[i - 1]
            rhs = inFixList[i + 1]
            merged = f"{lhs} {rhs} {c}"
            inFixList[i - 1 : i + 2] = [merged]
            i = max(0, i - 1)  
        else:
            i += 1

   return " ".join(inFixList)
