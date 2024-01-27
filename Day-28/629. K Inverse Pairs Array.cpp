#include<vector>
using namespace std;
class Solution {
private:
    int MOD = 1e9+7;
    int solve(int n, int k, vector<vector<int>>&dp){
        if(k <= 0) return k == 0;
        if(dp[n][k] != -1) return dp[n][k];

        int ans = 0;
        for (int i = 0; i <= k && i < n; i++) {
            ans = (ans + solve(n - 1, k - i, dp)) % MOD;
        }

        return dp[n][k] = ans;
    }

public:
    int kInversePairs(int n, int k) {
        vector<vector<int>>dp(n+1, vector<int>(k+1, -1));
        return solve(n, k, dp);
    }
};