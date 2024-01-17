
# Problem Link:
#     https://leetcode.com/problems/unique-number-of-occurrences/?envType=daily-question&envId=2024-01-17

from ast import List
from collections import Counter


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        return len(set(Counter(arr).values()))==len(Counter(arr))