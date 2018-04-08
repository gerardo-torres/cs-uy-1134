# Created by: Gerardo Torres
# cs-uy 1134

# n is an integer, n >= 1
def power(x, n): # run time of n
    """ Recursive implementation of an x to the n. """
    if n == 1:
        return x
    else:
        rest = power(x, n - 1)
        return x * rest

print(power(3, 2))

# n is an integer, n >= 1
def power2(x, n):
    """ Recursive implementation of an x to the n in
    runtime n. """
    if n == 1:
        return x
    else:
        part_1 = power2(x, n // 2)
        part_2 = power2(x, n // 2)
        if n % 2 == 0:
            return part_1 * part_2
        else:
            return x * part_1 * part_2


def power3(x, n):
""" Recursive implementation of an x to the n in
runtime log(n). """
if n == 1:
    return x
else:
    part = power3(x, n // 2)
    if n % 2 == 0:
        return part * part
    else:
        return x * part * part