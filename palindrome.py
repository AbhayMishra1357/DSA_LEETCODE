# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         s=s.lower().replace(" " , "").replace(":" , "").replace("," , "")
        
#         print(s)
#         res = s[::-1]
#         print(res)
#         if res == s:
#             return True
#         else:
#             return False
        
# a=Solution()
# print(a.isPalindrome("A man, a plan, a canal: Panama"))
                        #sol 2
# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         filtered = ""
#         for char in s:
#             if char.isalnum():  # Check if the character is alphanumeric
#                 filtered += char.lower()  # Convert to lowercase and add to the filtered string
        
#         # Check if the filtered string is equal to its reverse
#         return filtered == filtered[::-1]

# a = Solution()
# print(a.isPalindrome("A man, a plan, a canal: Panama"))  # Output: True

                        #sol 3



class Solution:
    def isPalindrome(self, s: str) -> bool:
        res=""
        for i in s:
            if i.isalnum():
                res=res+i.lower()
        return res == res[::-1]
a = Solution()
print(a.isPalindrome("A man, a plan, a canal: Panama")) 