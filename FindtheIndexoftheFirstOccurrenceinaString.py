class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack):
            return -1
        elif needle == haystack:
            return 0
        for i in range(len(haystack)):
            if i + len(needle) <= len(haystack):
                if haystack[i:i+len(needle)] == needle:
                    return i
        return -1


sol = Solution()
print(sol.strStr(haystack = "abc", needle = "c"))



