class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        for i in range(len(nums)):
            nums[i] = nums[i] * nums[i]
            # print(nums)

        for i in range(len(nums)):
            for j in range(0,len(nums)-i-1):
                if nums[j] > nums[j+1]:
                    temp = nums[j]
                    nums[j]=nums[j+1]
                    nums[j+1] = temp

        return(nums)



a=Solution()
# print(a.sortedSquares([-4,-1,0,3,10]))
print(a.sortedSquares([-5,-3,-2,-1]))
        
