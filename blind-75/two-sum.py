from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        elem = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in elem:
                return [i,elem[diff]]
            elem[n] = i
        return 