class Solution:
    def differenceOfSum(self, nums: list[int]) -> int:
        res=0
        s=""
        a=0
        for i in range(len(nums)):
            a=a+nums[i]
            s+=str(nums[i])
        # print(a)
        # print(s)
        for i in range(len(s)):
            res+=int(s[i])
        # print(res)

        return a - res
nums=[1,15,6,3]
a=Solution()
print(a.differenceOfSum(nums))
