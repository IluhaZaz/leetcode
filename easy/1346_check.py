class Solution:
    def checkIfExist(self, arr: list[int]) -> bool:
        for i in range(len(arr)):
            if arr[i]*2 in arr[:i] + arr[i+1:]:
                return True
        return False