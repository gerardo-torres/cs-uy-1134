# Created by: Gerardo Torres
# Net ID: N15561823
# Question 3a

def square_root(num):
    pass

def square_root_2(num):
    """ Calculates the square root of a number to the nearest two decimals. """
    possible_square_root = 0.01
    found_square_root = False
    while !found_square_root:
        check_val = possible_square_root * possible_square_root
        if round(check_val, 2) == num:
            found_square_root = True
        else:
            possible_square_root += 0.01
    return possible_square_root