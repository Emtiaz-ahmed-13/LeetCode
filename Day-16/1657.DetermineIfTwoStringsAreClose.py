# Problem Link:
#     https://leetcode.com/problems/determine-if-two-strings-are-close/

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:

        if len(word1) !=len(word2):
            return False
        
        count1=Counter(word1)
        count2=Counter(word2)

        cdn1=sorted(count1.keys()) == sorted(count2.keys())
        cdn2=sorted(count1.values()) == sorted(count2.values())
        return cdn1 and cdn2
        


        

