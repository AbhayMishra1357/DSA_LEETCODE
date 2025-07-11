'''
1486. XOR Operation in an Array
Easy
Topics
premium lock icon
Companies
Hint
You are given an integer n and an integer start.

Define an array nums where nums[i] = start + 2 * i (0-indexed) and n == nums.length.

Return the bitwise XOR of all elements of nums.

 

Example 1:

Input: n = 5, start = 0
Output: 8
Explanation: Array nums is equal to [0, 2, 4, 6, 8] where (0 ^ 2 ^ 4 ^ 6 ^ 8) = 8.
Where "^" corresponds to bitwise XOR operator.'''

class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        res=0
        for i in range(n):
            num = start + 2*i
            res^=num
        return res
            
                

        
a=Solution()
print(a.xorOperation(5,0))
print(a.xorOperation(4,3))
