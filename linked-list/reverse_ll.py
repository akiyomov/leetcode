class Node:
    def __init__(self, val: int):
        self.val = val
        self.next = None
def reverse_list(head: Node) -> Node:
    curr = head
    prev = None
    while curr is not None:
        next_ = curr.next
        curr.next = prev
        prev = curr
        curr = next_
    return prev
