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

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        cntr, w, matched = Counter(s1), len(s1), 0   

        for i in range(len(s2)):
            if s2[i] in cntr: 
                cntr[s2[i]] -= 1
                if cntr[s2[i]] == 0:
                    matched += 1
            # explanation: if w = 3, i = 3, then we need to check if s2[0] is in cntr
            # if w = 3, i = 4, then we need to check if s2[1] is in cntr
            if i >= w and s2[i-w] in cntr: 
                if cntr[s2[i-w]] == 0:
                    matched -= 1
                cntr[s2[i-w]] += 1

            if matched == len(cntr):
                return True

        return False

if __name__ == "__main__":
    print(check_permutation("abc","cba"))
    print(check_permutation("abc","cbad"))
 