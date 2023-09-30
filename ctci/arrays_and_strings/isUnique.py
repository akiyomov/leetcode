def isUnique(input_str):
    # O(n) time, O(1) space
    length = len(input_str)
    for i in range(length):
        for j in range(i+1,length):
            if input_str[i] == input_str[j]:
                return False