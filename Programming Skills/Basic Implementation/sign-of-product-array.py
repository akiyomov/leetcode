from typing import List

class Solution:
    def arraySign(self, nums: List[int]) -> int:
        def signFunc(x):
            if x == 0:
                return 0
            if x > 0:
                return 1
            return -1
        a = 1
        for i in nums:
            a *= i
        return signFunc(a)