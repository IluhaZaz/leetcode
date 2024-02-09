class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: list[int], target: int) -> int:
        return len(list(filter(lambda x: 1 if x >= target else 0, hours)))