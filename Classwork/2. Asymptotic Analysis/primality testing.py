def is_prime_1(num):
    """ Version 1: """
    count = 0
    for curr in range(1, num + 1):
        if num % curr == 0:
            count += 1
    if count == 2:
        return True
    else:
        return False


def is_prime_2(num):
    """ Version 2: ends at the halfway point of num"""
    count = 0
    for curr in range(1, (num / 2) + 1):
        if num % curr == 0:
            count += 1
    if count == 1:  # if we don't find anything in the first half, it's a prime.
        return True
    else:
        return False

def is_prime_3(num):
    """ Version 3: up to the sq root"""
    count = 0
    for curr in range(1, (num ** 0.5 ) + 1):
        if num % curr == 0:
            count += 1
    if count == 1: # if we don't find anything in the first part before the sq root, it's a prime.
        return True
    else:
        return False

""" is_prime1 > is_prime2 > is_prime3 """