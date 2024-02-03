class Solution:
    def duplicateZeros(self, arr: list[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        l = len(arr)
        str_arr = list(map(str, arr))
        buf = "".join(str_arr)
        buf = buf.replace("0", "00")
        for i in range(l):
            arr[i] = int(buf[i])

s = Solution()
arr = [1,0,2,3,0,4,5,0]
s.duplicateZeros(arr)
print(arr)



            