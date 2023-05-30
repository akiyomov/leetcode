class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle not in haystack:
            return -1
        i = len(needle)
        j = 0
        while True:
            if needle in haystack[j:j+i]:
                return j
            j += 1