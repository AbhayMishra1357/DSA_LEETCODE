'''3232. Find if Digit Game Can Be Won
Easy
Topics
premium lock icon
Companies
Hint
You are given an array of positive integers nums.

Alice and Bob are playing a game. In the game, Alice can choose either all single-digit numbers or all double-digit numbers from nums, and the rest of the numbers are given to Bob. Alice wins if the sum of her numbers is strictly greater than the sum of Bob's numbers.

Return true if Alice can win this game, otherwise, return false.

 

Example 1:

Input: nums = [1,2,3,4,10]

Output: false

Explanation:

Alice cannot win by choosing either single-digit or double-digit numbers.'''

class Solution:
    def canAliceWin(self, nums: list[int]) -> bool:
        alice=0
        bob=0

        # alice got single
        for i in range(len(nums)):
            if nums[i] < 10 :
                alice+=nums[i]
                print("Alice single ",alice)
            else : 
                bob+=nums[i]
                print("bob double",bob)
        if alice > bob:
            return True
        alice = 0
        bob = 0
        # alice got double  
        for i in range(len(nums)):
            if nums[i] > 9 :
                alice+=nums[i]
                print("Alice double ",alice)
            else : 
                bob+=nums[i]
                print("bob single",bob)
        if alice > bob:
            return True

        return False
        


a=Solution()
# print(a.canAliceWin([1,2,3,4,10]))
print(a.canAliceWin([5,5,5,25]))
