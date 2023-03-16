class Node:
    def __init__(self, val: int):
        self.val = val
        self.next = None
def remove_duplicates(head: Node) -> Node:
    curr = head
    while curr and curr.next:
        if curr.val == curr.next.val:
            curr.next = curr.next.next
            continue
        curr = curr.next
    return head

