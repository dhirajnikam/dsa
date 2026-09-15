import operator


def eval_rpn(tokens):
    # O(n) time, O(n) space
    # Operands go on a stack; an operator pops two (right operand first) and pushes the result.
    # int(a / b) truncates toward zero, unlike // which floors.
    ops = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": lambda a, b: int(a / b),
    }
    stack = []
    for tok in tokens:
        if tok in ops:
            b, a = stack.pop(), stack.pop()
            stack.append(ops[tok](a, b))
        else:
            stack.append(int(tok))
    return stack[0]
