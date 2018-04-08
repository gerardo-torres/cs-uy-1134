import random
def roll_the_dice_str (n):
    s = ""
    for i in range(1, n + 1):
        curr_val = random.randint(1, 6)
        s = s + str(curr_val) + " "
    return s[:- 1]

print(roll_the_dice_str(3))

def roll_the_dice_str_2(n):
    lst = n * [str(random.randint(1, 6))]
    return " ".join(lst)

print(roll_the_dice_str_2(4))