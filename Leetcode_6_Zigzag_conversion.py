class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        rows = ["" for _ in range(numRows)]
        length = len(s)
        cycle = (numRows * 2) - 2
        for i in range(length):
            if i % cycle > (numRows - 1):
                index = -abs((i % cycle) - (numRows - 2))
                rows[index] += s[i]
            else:
                rows[i % cycle] += s[i]
        result = ""
        for row in rows:
            result += row
        return result


s = Solution()
print(s.convert("PAYPALISHIRING", 1))
