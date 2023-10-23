class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        index = 0
        final = ""
        for letter in s:
            for i in range(index, len(t)):
                if letter == t[i]:
                    index = i + 1
                    final += letter
                    break

        if final == s:
            return True
        else:
            return False

sol = Solution()
print(sol.isSubsequence(s = "axc", t = "ahbgdc"))

