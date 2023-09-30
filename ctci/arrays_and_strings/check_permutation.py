def check_permutation(s1,s2):
    # O(nlogn) solution
    # O(n) space
    if len(s1) != len(s2):
        return False
    s1 = sorted(s1)
    s2 = sorted(s2)
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            return False
    return True

def check_permutation2(s1,s2):
    if len(s1) != len(s2):
        return False
    count = {}
    for i in s1:
        # count.get(i,0) returns the value of count[i] if i is in count, otherwise it returns 0
        count[i] = count.get(i,0) + 1
    for i in s2:
        if i in count:
            count[i] -= 1
            if count[i] == 0:
                del count[i]
        else:
            return False
    return len(count) == 0

print(check_permutation2("abc","cba"))
 