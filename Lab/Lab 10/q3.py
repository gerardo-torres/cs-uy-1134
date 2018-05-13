from DoublyLinkedList import *

def flatten_linked_lst(lnk_lst):
    """
    : lnk_lst type: DoublyLinkedList
    : return-value type: DoublyLinkedList
    """
    new = DoublyLinkedList()
    return flatten_linked_lst_helper(lnk_lst, lnk_lst.first_node(), new)

def flatten_linked_lst_helper(lnk_lst, node, new):
    while node.data is not None:
        if not isinstance(node.data, int):
            flatten_linked_lst_helper(lnk_lst, node.data.first_node(), new)
        else:
            new.add_last(node.data)
        node = node.next
    return new

def main():
    lnk_lst1 = DoublyLinkedList()
    elem1 = 1
    lnk_lst1.add_last(elem1)
    elem2 = DoublyLinkedList()
    elem2.add_last(2)
    elem2.add_last(3)
    lnk_lst1.add_last(elem2)
    elem3 = 4
    lnk_lst1.add_last(elem3)
    lnk_lst2 = flatten_linked_lst(lnk_lst1)
    print(lnk_lst1)
    print(lnk_lst2)

main()
