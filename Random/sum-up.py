arr = [1,2,3,4,5,6,7,8,9,10]
def sum_up(arr):
    if arr == []:
        return 0  
    return arr[0] + sum_up(arr[1:])

print(sum_up(arr))
# Find max element in array using recursion

def max_element(arr):
    if len(arr) == 2:
        return arr[0] if arr[0] > arr[1] else arr[1]
    submax = max(arr[1:])
    return arr[0] if arr[0] > submax else submax

print(max_element([1,2,3,4,5,6,7,8,9,10]))
        