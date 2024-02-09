class Solution:
    def interpret(self, command: str) -> str:
        d = {"()": "o", "(al)": "al"}
        for key, item in d.items():
            command = command.replace(key, item)
        return command