import random

def quicksort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot_index = random.randint(0, len(arr) - 1)
        pivot = arr[pivot_index]
        less = [i for i in arr if i < pivot]
        greater = [i for i in arr if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)
    
print(quicksort([9,5,7,3,8,4,1,6]))