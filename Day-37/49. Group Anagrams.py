#PROBLEM LINK:
    # https://leetcode.com/problems/group-anagrams/description/?envType=daily-question&envId=2024-02-06
    
# Since the output needs to group the anagrams, it is suitable to use dict to store the different anagrams.
# Thus, we need to find a common key for those anagrams.
# And one of the best choices is the sorted string as all the anagrams have the same anagrams.

# aet-ate,eat,tea
# ant-nat,tan
# abt-bat

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs_table = {}

        for string in strs:
            sorted_string = ''.join(sorted(string))

            if sorted_string not in strs_table:
                strs_table[sorted_string] = []

            strs_table[sorted_string].append(string)

        return list(strs_table.values())