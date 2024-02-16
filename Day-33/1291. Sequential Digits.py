

# PROBLEM LINK:
#         https://leetcode.com/problems/sequential-digits/?envType=daily-question&envId=2024-02-02

class Solution:
    def sequentialDigits(self, low, high):
        result = []
        
        for i in range(1, 10):
            num = i
            
            for j in range(i + 1, 10):
                num = num * 10 + j
                
                if low <= num <= high:
                    result.append(num)
        
        result.sort()
        return result