
from BinaryExpressionTree import BinaryExpressionTree


def run_one(expr):
    bet = BinaryExpressionTree()
    bet.build_from_postfix(expr)
    print("Infix Expression:", bet.inorder())
    print("Postfix Expression:", bet.postorder())
    print("Evaluated Result:", bet.evaluate())
    print()


if __name__ == "__main__":
    print("----- Binary Expression Tree -----")
    # Samples from the example set in instructions
    samples = [
        "5 3 +",
        "8 2 - 3 +",
        "5 3 8 * +",
        "6 2 / 3 +",
        "5 8 + 3 -",
        "5 3 + 8 *",
        "8 2 3 * + 6 -",
        "5 3 8 * + 2 /",
        "8 2 + 3 6 * -",
        "5 3 + 8 2 / -",
        "2 9 1 4 - / 3 1 - * 6 + *" # Bonus extra complicated sample question
    ]
    for s in samples:
        run_one(s)