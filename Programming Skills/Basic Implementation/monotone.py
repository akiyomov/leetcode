class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        inc = all(nums[i] <= nums[i+1] for i in range(len(nums) - 1))
        dec = all(nums[i] >= nums[i+1] for i in range(len(nums) - 1))
        return inc or dec
