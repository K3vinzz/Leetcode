from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        res = defaultdict(list)

        for str in strs:
            count = [0] * 26
            for letter in str:
                count[(ord(letter) - ord("a"))] += 1
            res[tuple(count)].append(str)

        return res.values()

s = Solution()
print(s.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))








