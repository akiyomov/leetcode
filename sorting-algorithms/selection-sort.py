def smallest_i(arr):
    smallest_num = arr[0]
    smallest_index = 0
    for i in range(1,len(arr)):
        if smallest_num > arr[i]:
            smallest_num = arr[i]
            smallest_index = i
    return smallest_index
print(smallest_i([5,3,6,2,10]))

def selection_sort(arr):
    new_arr = []
    for i in range(len(arr)):
        smallest = smallest_i(arr)
        new_arr.append(arr.pop(smallest))
    return new_arr

print(selection_sort([5,3,6,2,10]))
