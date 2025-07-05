'''Given a string s, return the string after replacing every uppercase letter with the same lowercase letter.

 

Example 1:

Input: s = "Hello"
Output: "hello"'''

# class Solution:
#     def toLowerCase(self, s: str) -> str:
#         return s.lower()

# without inbuild function
class Solution:
    def toLowerCase(self, s: str) -> str:
        for i in range(len(s)):
            if s[i] >= "A" and s[i] <= "Z":
                s = s[:i] + chr(ord(s[i]) + 32) + s[i+1:]
        return s
    
a = Solution()
print(a.toLowerCase("HELLO"))  
print(a.toLowerCase( "here"))  
