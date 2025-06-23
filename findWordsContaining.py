'''Input: words = ["leet","code"], x = "e"
Output: [0,1]
Explanation: "e" occurs in both words: "leet", and "code". Hence, we return indices 0 and 1.'''

class Solution:
    def findWordsContaining(self, words: list[str], x: str) -> list[int]:
        res=[]
        for i in range(len(words)):
            if x in words[i]:
                res.append(i)
        return res
    
a=Solution()
print(a.findWordsContaining(["leet","code"], x = "e"))
# print(a.findWordsContaining(["abc","bcd","aaaa","cbc"], x = "a"))
