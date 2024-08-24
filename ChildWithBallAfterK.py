# 3178. Find the Child Who Has the Ball After K Seconds
class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        n -= 1
        kid = k//n
        rem = k%n
        if kid % 2 == 0:
            return rem
        else:
            return n - rem