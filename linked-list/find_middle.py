class Node:
    def __init__(self, val: int):
        self.val = val
        self.next = None
def find_middle(head: Node) -> None:
    fast = slow = head

    while fast and fast.next is not None:
        fast = fast.next.next
        slow = slow.next
    
    print(slow.val)
    
