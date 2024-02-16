#PROBELM LINK:https://leetcode.com/problems/rearrange-array-elements-by-sign/description/?envType=daily-question&envId=2024-02-14

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        v1,v2,ans=[],[],[]
        
        # for possitive and negative number...!!!!
        for num in nums:
            if num>0:
                v1.append(num)
            else:
                v2.append(num)
        
        #track the indexing for the part...!!!
        ind1,ind2=0,0
        
        #equl number so i can divide it into 2part...!!!
        while ind2<len(nums)//2:
            ans.append(v1[ind1])
            ind1+=1
            ans.append(v2[ind2])
            ind2 +=1

        return ans
        
# t.c=0(n)
# s.c=0(n)



