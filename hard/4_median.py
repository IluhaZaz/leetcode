class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        ans = sorted(nums1 + nums2)
        l: int = len(ans)
        temp: int = int(l/2)
        if l%2 == 0:
            return (ans[temp] + ans[temp - 1])/2
        return ans[temp]
        