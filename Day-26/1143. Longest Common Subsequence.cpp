// PROBLEM LINK:https://leetcode.com/problems/longest-common-subsequence/?envType=daily-question&envId=2024-01-25

class Solution {
public:
//1-Initialization: Create a 2D array dp to store the lengths of LCS for various substrings. Initialize the array with zeros
//2- Dynamic Programming Iteration: Iterate through the substrings of the input strings in reverse order (from the end towards the beginning)
//3- LCS Calculation: For each pair of characters at the current positions (i, j) in text1 and text2, calculate the length of the LCS:

//4-If the characters match (text1[i] == text2[j]), increment the length of LCS by 1 (1 + dp[i+1][j+1]).

//5-If the characters don't match, take the maximum LCS length from the adjacent cells (max(dp[i+1][j], dp[i][j+1])).

//6- Store Results: Store the computed LCS length in the corresponding cell of the 2D array dp.

//7- Result Retrieval: The top-left cell of the 2D array (dp[0][0]) contains the length of the LCS for the entire strings.

//8-Return Result: Return the length of the LCS as the final result.
//Time complexity:0(n*n)
//Space complexity:0(n*2)
  int longestCommonSubsequence(string text1, string text2) {
        int n=text1.size();
        int m= text2.size();

        int dp[n+1][m+1];
        memset(dp,0,sizeof(dp));

        for(int i=n-1 ; i>=0 ; i--){
            for(int j=m-1 ; j>=0 ; j--){
                int result=0;
                if(text1[i]==text2[j]){
                    result = 1 + dp[i+1][j+1];
                }
                else{
                    result= max(dp[i+1][j] ,dp[i][j+1]);
                }
                dp[i][j]=result;
            }
        }

        return dp[0][0];
    }
};