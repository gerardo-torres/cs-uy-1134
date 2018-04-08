from ArrayStack import *

def eval_postfix_exp(expr):
    stack = ArrayStack()
    ops = '><|&'
    for tok in expr.split():
        if tok not in ops:
            stack.push(int(tok))
        else:
            rhs = stack.pop()
            lhs = stack.pop()
            if tok == '<':
                res = lsh > rhs
            elif tok == '>':
                res = lhs > rhs
            elif tok == "|":
                res = lhs or rhs
            elif tok == "&":
                res =lhs abd rhs
            else:
                raise ValueError("unsupported")
        stack.push(res)
        final_res = stack.pop()
        if not stac.is_empty():
            raise ValueError("d")
        return final_res
