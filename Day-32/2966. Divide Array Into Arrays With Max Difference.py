# Problem Link:
#     https://leetcode.com/problems/divide-array-into-arrays-with-max-difference/?envType=daily-question&envId=2024-02-01

class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        result = []
        for i in range(0, len(nums), 3):
            if i + 2 > len(nums) or nums[i+2] - nums[i] > k: return []    
            else: result.append(nums[i:i+3])
        return result
        