class Solution:
    def numberGame(self, nums: list[int]) -> list[int]:
        nums.sort() 
        res = []
        
        for i in range(0, len(nums), 2):
            alice = nums[i]
            bob = nums[i + 1]
            res.append(bob)   
            res.append(alice) 
        return res

a = Solution()
print(a.numberGame([5, 4, 2, 3])) 
