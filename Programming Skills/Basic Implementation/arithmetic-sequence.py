from typing import List


class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        new = sorted(arr)
        l = len(new)-1
        while l >= 2:
            if new[l] - new[l-1] != new[l-1] - new[l-2]:
                return False
            l -= 1

        return True
