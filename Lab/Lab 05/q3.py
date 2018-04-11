# Created by: Gerardo Torres
# Lab 5 Question 3

input_str = "boobs"

def is_palindrome(input_str, low, high):
    if low >= high:
        return True
    else:
        is_pal = is_palindrome(input_str, low + 1, high - 1)
        if input_str[low] != input_str[high]:
            is_pal = False
        return is_pal

print(is_palindrome(input_str, 0, len(input_str) - 1))
 x