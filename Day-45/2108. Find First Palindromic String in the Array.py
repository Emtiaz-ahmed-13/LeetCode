#PROBELM LINK: https://leetcode.com/problems/find-first-palindromic-string-in-the-array/description/?envType=daily-question&envId=2024-02-13

class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        # Iterate through each word in the list.
        for word in words:
            # Check if the current word is a palindrome by comparing it to its reversed version.
            if word == word[::-1]:
                # If a palindrome is found, return it immediately.
                return word
        # If no palindrome is found in the entire list, return an empty string.
        return ""

# Time complexity: O(M * N), where M is the number of words in the list and N is the average length of the words.
# Space complexity: O(1)