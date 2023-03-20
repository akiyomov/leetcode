from collections import Counter

def two_sum(arr: list[int], target: int) -> bool:
    """
    Kodni bu yerda yozing.
    """
    complements = {}
    for i,n in enumerate(arr):
        complements[target-n] = i
    for i,n in enumerate(arr):
        if n in complements and complements[n] != i:
            return True
    return False

def two_sum(arr):
    return Counter(arr).most_common()[0][0]