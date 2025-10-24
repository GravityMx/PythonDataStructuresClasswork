
from PostFixMathProgram.Stack import Stack

def PostFixEvaluation(postFixStr):

    stack = Stack()
    postFixList = postFixStr.split()

    for c in postFixList:
        # Test if this is a number or not
        if c.isdigit():
            stack.Push(int(c))
            continue

        # Parse for weather this is an opperation or not
        if (c == "+"):
            b = stack.Pop()
            a = stack.Pop()
            stack.Push(a + b)
            continue
        elif (c == "-"):
            b = stack.Pop()
            a = stack.Pop()
            stack.Push(a - b)
            continue
        elif (c == "*"):
            b = stack.Pop()
            a = stack.Pop()
            stack.Push(a * b)
            continue
        elif (c == "/"):
            b = stack.Pop()
            a = stack.Pop()
            stack.Push(a / b)
            continue
        else:
            return (f"Invalid opperation, the following charactor could not be parsed: {c}")

    if (stack.Length() == 1):
        return stack.Pop()
    else:
        return ("Invalid opperation, there were not exactly one more numerals then oppertaions")

