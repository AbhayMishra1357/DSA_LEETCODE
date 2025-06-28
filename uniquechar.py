'''Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

 

Example 1:

Input: s = "leetcode"

Output: 0

Explanation:

The character 'l' at index 0 is the first character that does not occur at any other index.'''
class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        for i in range(len(s)):
            is_uni=True
            for j in range(len(s)):
                if s[i] == s[j] and i!=j:
                    is_uni=False
                    break
                    # index = i
                    print(f"{res} in if")
            if is_uni:
                return i
        return -1
    
a=Solution()
# print(a.firstUniqChar("leetcode"))
print(a.firstUniqChar("loveleetcode"))

