def merge_two_arrays(arr1: list[int], arr2: list[int]) -> list[int]:
    result = []
    i, j = 0, 0
    n, m = len(arr1), len(arr2)
    while i < n and j < m:
        if arr1[i] < arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1
    while i < n:
        result.append(arr1[i])
        i+=1
    while i < m:
        result.append(arr2[j])
        j+=1
    return result
    
print(merge_two_arrays([1,3,5], [1,2,6]))