# problem Link:
#     https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/?envType=daily-question&envId=2024-01-23

class Solution:
    def maxLength(self, arr: list[str]) -> int:
        distinct = ['']
        maxLen = 0
        for i in range(len(arr)):
            current = distinct
            for j in range(len(current)):
                newStr = arr[i] + current[j]
                if len(set(newStr)) == len(newStr):
                    distinct.append(newStr)
                    s=len(newStr)
                    maxLen = max(maxLen,s)
        return maxLen
