class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return int(len(s.split()[-1]))


sol = Solution()
print(sol.lengthOfLastWord("a df  qwewq"))
