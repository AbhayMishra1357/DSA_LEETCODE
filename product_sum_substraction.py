'''Input: n = 234
Output: 15 
Explanation: 
Product of digits = 2 * 3 * 4 = 24 
Sum of digits = 2 + 3 + 4 = 9 
Result = 24 - 9 = 15'''

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        multi=1
        sum=0
        res=0
        s=str(n)
        for i in range(len(s)):
            multi=multi*int(s[i])
            sum+=int(s[i])
            print(f"{multi} and {sum}")
        
        res=multi-sum
        return res
a=Solution()
print(a.subtractProductAndSum(234))
