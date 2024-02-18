class Solution:
    def mostWordsFound(self, sentences: list[str]) -> int:
        return max([len(i.split()) for i in sentences])