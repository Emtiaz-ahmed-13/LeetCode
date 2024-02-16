#PROBELM LINK:https://leetcode.com/problems/least-number-of-unique-integers-after-k-removals/description/?envType=daily-question&envId=2024-02-16

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        m=Counter(arr)
        v=list(m.values())
        v.sort()
        count=0
        for i in range(len(v)):
            if k >v[i]:
                k-=v[i]
                v[i]=0
            else:
                v[i]-=k
                k=0
            if v[i] !=0:
                count+=1
        return count