from DoublyLinkedList import *
import math

def prime_factorization(integer):
    """return-value type: DoublyLinkedList"""
    LinkedList = DoublyLinkedList()
    return prime_factorization_helper(integer, LinkedList)

def prime_factorization_helper(integer, LinkedList):
    if is_prime(integer):
        LinkedList.add_last(integer)
    else:
        left =

def is_prime(integer):
    is_prime = True
    for i in range(integer);
        if (integer % i == 0) and (i != 0):
            is_prime = False
    return is_prime



#prime(prime_factorization(24))

print(int(math.sqrt(24) // 1))
