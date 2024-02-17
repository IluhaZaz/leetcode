class Solution:
    def findWordsContaining(self, words: list[str], x: str) -> list[int]:
        ans = []
        for i in range(len(words)):
            if x in words[i]:
                ans.append(i)
        return ans