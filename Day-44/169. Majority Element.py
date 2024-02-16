#PROBELM LINK: https://leetcode.com/problems/majority-element/description/?envType=daily-question&envId=2024-02-12


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 1
        ans = nums[0]
        for i in range(1, len(nums)):
            if nums[i] != ans:
                count -= 1
            else:
                count += 1
            
            if count == 0:
                ans = nums[i]
                count = 1
        
        return ans
