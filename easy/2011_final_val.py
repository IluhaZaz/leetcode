class Solution:
    def finalValueAfterOperations(self, operations: list[str]) -> int:
        x: int = 0
        for i in operations:
            if i in ("--X", "X--"):
                x -= 1
            else:
                x +=1
        return x