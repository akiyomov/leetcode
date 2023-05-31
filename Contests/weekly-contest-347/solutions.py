from typing import List


class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        i = len(num) - 1
        while i >= 0 and num[i] == '0':
            i -= 1
        if i == len(num) - 1:
            return num
        else:
            return num[:i+1]


class Solution:
    def differenceOfDistinctValues(self, grid: List[List[int]]) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        answer = [[0] * n for _ in range(m)]

        for r in range(m):
            for c in range(n):
                top_left = set()
                for i in range(r):
                    if c - (r - i) >= 0:
                        top_left.add(grid[i][c - (r - i)])
                bottom_right = set()
                for i in range(r + 1, m):
                    if c + (i - r) < n:
                        bottom_right.add(grid[i][c + (i - r)])
                answer[r][c] = abs(len(top_left) - len(bottom_right))

        return answer
