# Problem Link:
#     https://leetcode.com/problems/determine-if-string-halves-are-alike/

class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        string=s.lower()
        s="aeiou"
        n=int(len(string))
        h=int(n//2)
        c1=0
        c2=0
        for i in string[:h]:
            if i in s:
                c1+=1
        for j in string[h:]:
            if j in s:
                c2+=1
        if c1==c2:
            return True
        
        else:
            return False



        
        