# Problem Link:
#     https://leetcode.com/problems/house-robber/?envType=daily-question&envId=2024-01-21


class Solution:
    def rob(self, nums: list[int]) -> int:  
        rob1, rob2 = 0, 0  
        for i in nums:
            rob1, rob2 = rob2, max(rob1 + i, rob2)
        return rob2