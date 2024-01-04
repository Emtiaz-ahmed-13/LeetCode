
// problem link: 
//     https://leetcode.com/problems/minimum-number-of-operations-to-make-array-empty/
#include<iostream>
#include<unordered_map>
using namespace std;



class Solution {
public:
    int minOperations(vector<int>& nums) {
        unordered_map<int,int>m;
        for(auto a: nums)
        {
            m[a]++;
        }
        int count=0;
        for(auto a: m)
        {
            int t=a.second;
            if(t==1) return -1;
            count=count+ t/3;
            if(t%3) count++;
        }
        return count;
        
    }
};