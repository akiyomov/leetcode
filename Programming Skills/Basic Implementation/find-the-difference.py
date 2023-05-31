from collections import Counter


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        for k, v in (Counter(t)-Counter(s)).items():
            return k
        return ""
