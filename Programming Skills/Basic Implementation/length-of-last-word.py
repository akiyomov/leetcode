class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = -1
        c = 0
        while len(s) >= abs(i):
            a = s[i]
            if a != " ":
                c += 1
            i -= 1
            if a == " " and c > 0:
                break
        return c


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1])
