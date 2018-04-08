def permutations(lst,low,high): 
    if low == high:
        return [ lst ]

    res_perm = []
    for i in range(high-low + 1):
        lst_copy = lst[:]
        lst_copy[low],lst_copy[high-i]=lst_copy[high-i],lst_copy[low]
        res_perm.extend(permutations(lst_copy, low + 1, high))

    return res_perm

        
            

