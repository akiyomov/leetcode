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