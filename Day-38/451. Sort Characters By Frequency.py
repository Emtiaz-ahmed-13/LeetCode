#PROBLEM LINK:
    #https://leetcode.com/problems/sort-characters-by-frequency/description/?envType=daily-question&envId=2024-02-07

from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        k = Counter(s).most_common()  # Count frequencies and retrieve in descending order
        p = ''
        for i in range(0, len(k)):
            p += k[i][0] * k[i][1]  # Concatenate characters according to their frequencies
        return p
