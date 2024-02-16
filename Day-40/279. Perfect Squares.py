#PROBELM LINK:
    #https://leetcode.com/problems/perfect-squares/description/?envType=daily-question&envId=2024-02-08
    
class Solution:
    def numSquares(self, n: int) -> int:
        if n==0:
            return 0
        if n<0:
            return float("inf")
        mini=n
        while(i*j<=n):
            mini=min
            