def powers_of_two(num):
    start = 1
    while start <= num:
        yield 2 ** start
        start += 1

for curr_value in powers_of_two(6):
    print(curr_value)

