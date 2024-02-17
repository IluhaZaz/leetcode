class Solution:
    def shuffle(self, nums: list[int], n: int) -> list[int]:
        c: int = 0
        ans = [None for i in range(2*n)]
        for i, j in zip(nums[:n], nums[n:]):
            ans[c] = i
            ans[c + 1] = j
            c += 2
        return ans