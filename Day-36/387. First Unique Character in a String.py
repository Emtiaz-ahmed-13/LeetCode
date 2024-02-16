#PROBLEM LINK:
    # https://leetcode.com/problems/first-unique-character-in-a-string/description/?envType=daily-question&envId=2024-02-05
    
class Solution:
    def firstUniqChar(self, s: str) -> int:
        for i,c in enumerate(s):
            if s.count(c)==1:
                return i
                break
        return -1
