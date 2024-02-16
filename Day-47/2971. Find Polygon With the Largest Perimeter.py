#PROBELM LINK:https://leetcode.com/problems/find-polygon-with-the-largest-perimeter/?envType=daily-question&envId=2024-02-15

# Sort the array: Start by sorting the array of numbers in ascending order.

# Initialize variables: Set up variables to track the running sum (sum) and the largest perimeter found so far (ans).

# Iterate through the sorted array: Loop through each number in the sorted array.

# Check polygon condition: For each number, check if it's smaller than the sum of all previous numbers encountered.

# Update largest perimeter: If the condition is met, update ans with the sum of the current number and the running sum. Finally, return the largest perimeter found (ans).


class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        sum_val = 0
        ans = -1
        
        for num in nums:
            if num < sum_val:
                ans = num + sum_val
            sum_val += num
            
        return ans
