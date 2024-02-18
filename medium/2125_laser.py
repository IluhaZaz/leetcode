class Solution:
    def numberOfBeams(self, bank: list[str]) -> int:

        ans: int = 0

        bank = list(filter(lambda x: 0 if x.replace("0", "") == "" else 1, bank))

        devices = [row.count("1") for row in bank]
        for i in range(len(devices) - 1):
            ans += devices[i] * devices[ i + 1]
        return ans