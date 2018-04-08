def binary_search(srt_lst, val, low, high):
    curr = (low + high) / 2
    if curr < val:
        

lst = [1, 3, 4, 5, 6, 9, 12, 14, 18]

print(binary_search(lst, 6, 0, len(lst)))