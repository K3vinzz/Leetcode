class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        shortest = strs[0]
        for item in strs:
            if len(item) < len(shortest) and not len(item) == 0:
                shortest = item
            elif len(item) == 0:
                return ""

        for i in range(len(shortest), 0, -1):
            is_same = True
            for item in strs:
                if not item[:i] == shortest[:i]:
                    is_same = False
            if is_same:
                return shortest[:i]

        return ""




                # print(shortest[:i])
                # print(item[:i])





sol = Solution()
print(sol.longestCommonPrefix(["flower","flow","flight"]))



