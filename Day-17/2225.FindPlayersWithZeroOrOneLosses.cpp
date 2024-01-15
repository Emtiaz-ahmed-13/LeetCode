

// Prolem Link:
//     https://leetcode.com/problems/find-players-with-zero-or-one-losses/

#include<iostream>
#include<vector>
#include<map>
using namespace std;

class Solution {
public:
    vector<vector<int>> findWinners(vector<vector<int>>& matches) {
//need to map for store win or loss player track..
        map<int, int> win;
        map<int, int>loss;
//A 2D vector ans is initialized to store the results. It has two rows, one for players with wins and no losses, and the other for players with exactly one loss.
        vector<vector<int>> ans(2, vector<int>());
//wins and losses matchs..
        for(int i =0;i<matches.size();i++)       
        {
            win[matches[i][0]]++;
            loss[matches[i][1]]++;
        }
//now who is win and who is loss 
//If a player has at least one win (i->second > 0) and no losses (loss[i->first] == 0), the player is added to the first row of the ans vector
        for(auto i = win.begin();i !=win.end();i++)
         if((i->second > 0) && (loss[i->first] == 0))
        {
            ans[0].push_back(i->first);
        }
//If a player has one loss (i->second == 1), the player is added to the second row of the ans vector.
        for(auto i = loss.begin() ; i != loss.end() ; i++) {
            if(i->second == 1)
                ans[1].push_back(i->first);
        }
        return ans;
        
    }
};