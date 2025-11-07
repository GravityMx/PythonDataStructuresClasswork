
from Stack import Stack
from Node import Node

class BinaryExpressionTree:

    def __init__(self):

        self._root = None

    def build_from_postfix(self, expr_str: str):
        tokens = expr_str.split()
        ops = {"+","-","*","/","^"}
        st = Stack()
        # Go through each token
        for tok in tokens:
            if tok.replace(".","",1).isdigit(): # Test if this token is a number, if so it is a leaf and will be pushed
                st.push(_Node(tok))
            elif tok in ops: # If an opperation, pop in the two places indicated below, and make them into a node jointed together by this opperation 
                if st.is_empty(): print("Attempted opperation without left opperand") 
                right = st.peek() 
                st.pop()
                if st.is_empty(): print("Attempted opperation without right opperand")
                left = st.peek()
                st.pop()
                st.push(_Node(tok, left, right))
            else:
                print("Attempted to use an invalid token")
        if st.is_empty(): print("Attempted to build a tree with an empty string input")
        self._root = st.peek() 
        st.pop()

    # --- traversals ---
    def postorder(self) -> str:
        out = []
        self._post(self._root, out) 
        return " ".join(out)
    def _post(self, p, out):
        if p is None: return
        self._post(p.left, out) 
        self._post(p.right, out) 
        out.append(p.val)

    def inorder(self) -> str:
        return self._in(self._root)
    def _in(self, p) -> str:
        if p is None: return ""
        if p.left is None and p.right is None: return p.val
        return f"({self._in(p.left)} {p.val} {self._in(p.right)})"

    def evaluate(self) -> float:
        return self._eval(self._root)
    def _eval(self, p) -> float:
        if p is None: print("empty tree")
        if p.left is None and p.right is None:
            return float(p.val)
        x = self._eval(p.left) 
        y = self._eval(p.right)
        op = p.val
        if op == "+": return x + y
        if op == "-": return x - y
        if op == "*": return x * y
        if op == "/": return x / y
        print(f"unsupported operator: {op}")
        
