class Solution:
    def threeConsecutiveOdds(self, arr: list[int]) -> bool:
        for i in range(len(arr) - 2):  # Stop at len(arr) - 2 to avoid IndexError
            if arr[i] % 2 != 0 and arr[i+1] % 2 != 0 and arr[i+2] % 2 != 0:
                return True
        return False

a = Solution()
print(a.threeConsecutiveOdds([2, 3, 4, 1]))  # Output: False
print(a.threeConsecutiveOdds([1, 3, 5, 7]))  # Output: True
