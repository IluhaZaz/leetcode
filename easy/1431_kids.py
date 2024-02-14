class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        m = max(candies)
        return list(map(lambda x: True if x + extraCandies >= m else False, candies))