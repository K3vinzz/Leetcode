class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        output = []
        if len(nums) == 1:
            output.append(f"{nums[0]}")
        left = -1
        right = 1
        front = 0
        for r in range(right, len(nums)):
            left += 1
            if not (nums[r] - nums[left]) == 1 and not nums[front] == nums[left]:
                if r == len(nums) - 1 and not nums[front] == nums[left]:
                    output.append(f"{nums[front]}->{nums[left]}")
                    output.append(f"{nums[r]}")
                # elif r == len(nums) - 1 and nums[front] == nums[left]:
                #     output.append(f"{nums[front]}")
                else:
                    output.append(f"{nums[front]}->{nums[left]}")
                    left = r - 1
                    front = r
            elif not (nums[r] - nums[left]) == 1 and nums[front] == nums[left]:
                if r == len(nums) - 1:
                    output.append(f"{nums[front]}")
                    output.append(f"{nums[r]}")
                else:
                    output.append(f"{nums[front]}")
                    left = r - 1
                    front = r
            else:
                if r == len(nums) - 1:
                    output.append(f"{nums[front]}->{nums[r]}")
        return output

sol = Solution()
print(sol.summaryRanges(nums = [0,1,2,4,5,7]))