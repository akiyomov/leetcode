from typing import List

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        nums = []
        for var in operations:
            if var.isdigit() or var.startswith("-"):
                score = int(var)
                nums.append(score)
            elif var == "+":
                score = nums[-1] + nums[-2]
                nums.append(score)
            elif var == "D":
                score = 2 * nums[-1]
                nums.append(score)
            elif var == "C":
                nums.pop()
        return sum(nums)
