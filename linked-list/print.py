class Node:
    def __init__(self, val: int):
        self.val = val
        self.next = None

def print_elements(head: Node) -> None:
    if head is None:
        return
    print(head.val)
    print_elements(head.next)

