class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        numSet = set(nums)
        longest = 0
        for i in numSet:
            if i - 1 not in numSet:
                length = 0
                print(f"i = {i}")
                while i + length in numSet:
                    length += 1
                if length > longest:
                    longest = length
        return longest


s = Solution()
print(s.longestConsecutive([100,4,200,1,3,2]))



