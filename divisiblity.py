'''Input: n = 10, m = 3
Output: 19
Explanation: In the given example:
- Integers in the range [1, 10] that are not divisible by 3 are [1,2,4,5,7,8,10], num1 is the sum of those integers = 37.
- Integers in the range [1, 10] that are divisible by 3 are [3,6,9], num2 is the sum of those integers = 18.
We return 37 - 18 = 19 as the answer.'''

class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        divisible=[]
        nondivisible=[]
        num1=0
        num2=0
        for i in range (1,n+1):
            if i % m == 0 :
                divisible.append(i)
                num1+=int(i)
        print(divisible)
        print(num1)

        for i in range (1,n+1):
            if i % m != 0 :
                nondivisible.append(i)
                num2+=int(i)
        print(nondivisible)
        print(num2)
        return num2 - num1

a=Solution()
print(a.differenceOfSums( n=10 , m = 3))

