class Solution:
    def theMaximumAchievableX(self, num: int, t: int) -> int:
        while t>0:
            num = num+2
            t-=1
        return num
a=Solution()
print(a.theMaximumAchievableX(num = 4, t = 1))
print(a.theMaximumAchievableX(num = 3, t = 2))
