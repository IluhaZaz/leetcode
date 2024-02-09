class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        ans = 0
        jewels = set(jewels)
        for jew in jewels:
            ans += stones.count(jew)
        return ans