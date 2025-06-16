class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        nums1 = set(nums1)
        nums2 = set(nums2)

        results = nums1 & nums2

        return list(results)
    
Solution = Solution()
nums1 = [1,2,2,1]
nums2 = [2,2]
print(Solution.intersection(nums1 , nums2))