'''Example 2:

Input: n = 10
Output: 40
Explanation: Numbers in the range [1, 10] that are divisible by 3, 5, or 7 are 3, 5, 6, 7, 9, 10. The sum of these numbers is 40.'''
class Solution:
    def sumOfMultiples(self, n: int) -> int:
        res=0
        for i in range(1,n+1):
            if i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
                res+=i
                print(f"{res} in 3 if")
            # elif i % 5 == 0:
            #     res+=i
            #     print(f"{res} in 5 if")              
            # elif i % 7 == 0:
            #     res+=1  
            #     print(f"{res} in 7 if")
        return res
a=Solution()
print(a.sumOfMultiples(10))
print(a.sumOfMultiples(7))
