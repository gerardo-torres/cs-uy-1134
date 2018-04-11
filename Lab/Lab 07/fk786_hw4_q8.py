def flat_list(nested_lst,low,high):
    if (low==high):
        if (isinstance(nested_lst[low],list)!=True):
            return [nested_lst[low]]
        else:
            return flat_list(nested_lst[low],0,len(nested_lst[low])-1)
    else:
        flat_list_rest=flat_list(nested_lst,low+1,high)
        if isinstance(nested_lst[low],list):
            return flat_list(nested_lst[low],0,len(nested_lst[low])-1)+flat_list_rest
        else:
            return [nested_lst[low]]+flat_list_rest
