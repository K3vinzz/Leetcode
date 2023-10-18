class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        i = 0
        for num in nums:
            try:
                if nums.index(target - num) != i:
                    return [i, nums.index(target-num)]
                elif nums.index(target - num) == nums[i]:
                    pass
            except ValueError:
                pass
            i += 1

sol = Solution()
print(sol.twoSum(nums = [3,2,4], target = 6))


