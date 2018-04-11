from ArrayStack import *

boolean = ArrayStack()
argument = ArrayStack()
operator = ArrayStack()
boolean.push(&)

# & = AND
# | = OR

expression = "5 2 <"

def eval_postfix_boolean_exp(boolean_exp_str):
    boolean_str = "&|"
    opeator_str = "<>"
    boolean_exp_lst = boolean_exp_str.split()
    for i in range(len(boolean_exp_lst)):
        if boolean_exp_lst[i] in boolean_str:
            boolean.push(boolean_exp_lst[i])
        elif boolean_exp_lst[i] in opeator_str:
            operator.push(boolean_exp_lst[i])
        elif boolean_exp_lst[i] == " ":
            pass
        else:
            argument.push(boolean_exp_lst[i])

    for i in range(len(boolean) + 1):
        if bool_XD == "&":
            opp = operator.pop()
            if opp == "<":
                right = argument.pop()
                left = argument.pop()
                result = left < right
            elif opp == ">":
                right = argument.pop()
                left = argument.pop()
                result = left > right

print(eval_postfix_boolean_exp(expression))
