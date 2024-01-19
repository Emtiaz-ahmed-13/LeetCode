// problem link:
//      https://leetcode.com/problems/minimum-falling-path-sum/?envType=daily-question&envId=2024-01-19

#include<iostream>
#include<vector>
using namespace std;


class Solution {
public:
    int solve(int i, int j, vector<vector<int>> &matrix, vector<vector<int>>&dp){
        int n = matrix.size();
        if(j>=n || j<0) return 1e8;
        if(i==n-1) return matrix[i][j];
        if(dp[i][j] != 1e8) return dp[i][j];
        

        int leftdown = solve(i+1, j-1, matrix, dp);
        int down = solve(i+1, j, matrix, dp);
        int rightdown = solve(i+1, j+1, matrix, dp);
        return dp[i][j] = matrix[i][j] + min(leftdown, min(down, rightdown));
    }
    int minFallingPathSum(vector<vector<int>>& matrix) {
        int n = matrix.size();
        vector<vector<int>> dp(n, vector<int>(n, 1e8));
        int ans = 1e8;
        for(int i=0; i<n; i++){
            int temp = solve(0, i, matrix, dp);
            ans = min(ans, temp);
        }
        return ans;
    }
};