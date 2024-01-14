# Problem Link:
#     https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram/description/

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        return sum((Counter(t)-Counter(s)).values())