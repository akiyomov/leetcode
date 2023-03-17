from collections import Counter,defaultdict
from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        a = defaultdict(int)
        for i in nums:
            a[i] += 1
        maximum = max(a.values())
        for i in nums:
            if a[i] - maximum == 0:
                return i