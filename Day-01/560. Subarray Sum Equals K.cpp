// problem link:
//     https://leetcode.com/problems/subarray-sum-equals-k/




// The time complexity of this solution is O(nlogn) 
#include <iostream>
#include <vector>

using namespace std;
class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        int n = nums.size();
        unordered_map<int,int> cnt; 
        int sum=0;
        cnt[sum] = 1;

        int ans = 0;
        for (int ele : nums) {
            sum += ele;
            if (cnt[sum-k] > 0)
                ans += cnt[sum-k];
            cnt[sum] ++;
        }
        return ans;
    }
};