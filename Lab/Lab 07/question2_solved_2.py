from ArrayStack import *

def eval_postfix_exp(expr):
    stack = ArrayStack()
    ops = '><|&'
    lst = expr.split()
    for i in range(len(lst)):
        curr = lst[i]
        if curr not in ops:
            stack.push(int(curr))
        else:
            rhs = stack.pop()
            lhs = stack.pop()
            if curr == '<':
                res = lhs < rhs
            elif curr == '>':
                res = lhs > rhs
            elif curr == '&':
                res = lhs and rhs
            elif curr == "|":
                res = lhs or rhs
            stack.push(res)
    return stack.pop()

def main():
    print(eval_postfix_exp('1 2 < 6 3 < |'))

main()
