
// Problem Link:
//     https://leetcode.com/problems/valid-parentheses/




// We use a stack to maintain a order which is usuable to us in this case.
// Opening brackets we push to the stack
// and compare closing bracket and what is at the top
// If they make a pair
// We pop the stack and move forward
// and in the end check the size of the stack.
// If zero size we have a valid parenthesis if not then we dont have
// Complexity
// Time complexity:
// O(N)- length of string

// Space complexity:
// O(N)- using a stack
#include <string.h>
#include <stack>
#include <iostream>
using namespace std;

class Solution {
public:
    bool isValid(string s) {
        stack<char>helper;

        int i=0;
        while(i<s.length()){
        
                if(s[i]==')' && helper.size()>0 && helper.top()=='('){
                    helper.pop();
                }
                else  if(s[i]=='}' && helper.size()>0 && helper.top()=='{'){
                    helper.pop();
                }
                else  if(s[i]==']' && helper.size()>0 && helper.top()=='['){
                    helper.pop();
                }
                else{
                    helper.push(s[i]);
                }
                i++;
        }
                

            if(helper.size()==0){
                return true;
            }
            return false;
       
        }
       
};