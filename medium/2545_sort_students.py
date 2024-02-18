import pandas as pd


class Solution:
    def sortTheStudents(self, score: list[list[int]], k: int) -> list[list[int]]:
        df:pd.DataFrame = pd.DataFrame(data=score)
        df = df.sort_values(by=k)
        return df.values.tolist()


s = Solution()
print(s.sortTheStudents([[10,6,9,1],[7,5,11,2],[4,8,3,15]], 2))


class Solution:
    def sortTheStudents(self, score: list[list[int]], k: int) -> list[list[int]]:
        return sorted(score, key=lambda x: x[k], reverse=True)


s = Solution()
print(s.sortTheStudents([[10,6,9,1],[7,5,11,2],[4,8,3,15]], 2))