class Solution:
    def climbStairs(self, n: int) -> int:
        """
        You are climbing a stair case. It takes n steps to reach to the top.
        Each time you can either climb 1 or 2 steps.
        In how many distinct ways can you climb to the top?
        :param n: number of steps
        :return: number of distinct ways to climb to the top
        """
        if n <= 2:
            return n

        one, two = 1, 1
        for i in range(n - 1):
            temp = one
            one = one + two
            two = temp
        return one

example = Solution()
print(example.climbStairs(5))