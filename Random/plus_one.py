from typing import List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] == 9:
            digits = int(''.join(map(str, digits))) + 1
            return list(map(int, str(digits)))
        digits[-1] += 1
        return digits

