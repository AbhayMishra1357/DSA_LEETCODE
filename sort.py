# Given an array nums, return true if the array was originally sorted in non-decreasing order, then rotated some number of positions (including zero). Otherwise, return false.

# There may be duplicates in the original array.

# Note: An array A rotated by x positions results in an array B of the same length such that B[i] == A[(i+x) % A.length] for every valid index i.

class Solution:
    def check(self, nums: list[int]) -> bool:
        count = 0
        for i in range(len(nums)):
            if nums[i] > nums[(i + 1) % len(nums)]:
                count += 1
        return count <= 1
a=Solution()
print(a.check([1,2,3])) 
print(a.check([3,4,5,1,2])) 
