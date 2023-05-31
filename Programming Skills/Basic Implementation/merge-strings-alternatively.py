class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        l1 = len(word1)
        l2 = len(word2)
        min_length = min(l1, l2)
        word = ""
        while i < min_length:
            word += word1[i] + word2[i]
            i += 1
        if i < l1:
            return word + word1[i:]
        if i < l2:
            return word + word2[i:]
        return word
