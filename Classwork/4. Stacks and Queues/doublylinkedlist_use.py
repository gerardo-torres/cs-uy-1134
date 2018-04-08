import DoublyLinkedList

def remove_all(lnk_lst, item):
    """ removes all instances of 'item' in a linked list 'lnk_lst' """
    if lnk_lst.is_empty():
        return
    cursor = lnk_lst.first_node()
    while cursor is not lnk_lst.trailer:
        if item == cursor.data:
            next_node = cursor.next
            lnk_lst.delete_node(cursor)
            cursor = next_node
        else:
            cursor = cursor.next

def max_in_lnk_list(lnk_lst):
    """ recursive implementation to find a maximum value in a lninked list 'lnk_lst' """
    return max_in_sub_lnk_list(lnk_lst, lnk_lst.first_node())

def max_in_sub_lnk_list(lnk_lst, sublist_head):
    """ helper function for max_in_lnk_list """
    if sublist_head.next is lnk_lst.trailer:
        return sublist_head.data
    else:
        call = max_in_sub_lnk_list(lnk_lst, sublist_head.next)
        return max(call, sublist_head.data)

def average_compression(lnk_lst, k):
    if lnk_lst.is_empty():
        return
    cursor = lnk_lst.first_node()
    while cursor is not lnk_lst.trailer:
        curr_sum = 0
        for i in range(k):
            curr_sum += cursor.data
            next_node = cursor.next
            lnk_lst.delete_node()
            cursor = next_node
        curr_average = curr_sum / k
        lnk_lst.add_before = curr_sum / k



def max_in_list(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        call = max_in_list(lst[1:])
        return max(call, lst[0])

def main():
    lnk_lst1 = DoublyLinkedList.DoublyLinkedList()
    lnk_lst1.add_last(10)
    lnk_lst1.add_last(20)
    lnk_lst1.add_last(35)
    lnk_lst1.add_last(56)
    print(lnk_lst1)
    remove_all(lnk_lst1, 10)
    print(lnk_lst1)
    print(max_in_lnk_list(lnk_lst1))


main()