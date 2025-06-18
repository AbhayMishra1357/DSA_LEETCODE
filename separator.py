class Solution:
    def splitWordsBySeparator(self, words: list[str], separator: str) -> list[str]:
        self.separator = separator
        print(self.separator)
        res = []
        for word in words:
            if self.separator in word:
                res.extend(word.split(self.separator))
            else:
                res.append(word)
        return res
    
a=Solution()
print(a.splitWordsBySeparator(words = ["one.two.three","four.five","six"], separator = "."))
print(a.splitWordsBySeparator(words = ["$easy$","$problem$"], separator = "$"))

# class Solution:
#     def splitWordsBySeparator(self, words: list[str], separator: str) -> list[str]:
#         res = []
#         for word in words:
#             if separator in word:
#                 res.extend([part for part in word.split(separator) if part])  # Filter out empty strings
#             else:
#                 res.append(word)
#         return res
    
# a = Solution()
# print(a.splitWordsBySeparator(words=["one.two.three", "four.five", "six"], separator="."))
# print(a.splitWordsBySeparator(words=["$easy$", "$problem$"], separator="$"))