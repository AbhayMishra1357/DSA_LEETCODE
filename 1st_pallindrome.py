'''2108. Find First Palindromic String in the Array
Easy
Topics
premium lock icon
Companies
Hint
Given an array of strings words, return the first palindromic string in the array. If there is no such string, return an empty string "".

A string is palindromic if it reads the same forward and backward.

 

Example 1:

Input: words = ["abc","car","ada","racecar","cool"]
Output: "ada"
Explanation: The first string that is palindromic is "ada".
Note that "racecar" is also palindromic, but it is not the first.'''

class Solution:
    def firstPalindrome(self, words: list[str]) -> str:
        for i in range(len(words)):
            a=words[i]
            # print(a[:])
            # print(a[::-1])
            
            if a[:] == a[::-1]:
                return a
            
        return f" "
            
a=Solution()
# print(a.firstPalindrome(["abc","car","ada","racecar","cool"]))
print(a.firstPalindrome(["def","ghi"]))
        
