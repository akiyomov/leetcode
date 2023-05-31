class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return True if s in (s+s)[1:-1] else False
