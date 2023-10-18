class Solution:
    def maxArea(self, height: list[int]) -> int:
        result = 0
        l_ptr, r_ptr = 0, len(height) - 1
        while l_ptr < r_ptr:
            result = max(result, (r_ptr - l_ptr) * min(height[r_ptr], height[l_ptr]))
            if height[l_ptr] < height[r_ptr]:
                l_ptr += 1
            elif height[l_ptr] > height[r_ptr]:
                r_ptr -= 1
            elif height[l_ptr] == height[r_ptr]:
                l_ptr += 1
        return result

s = Solution()
print(s.maxArea([1,2,1]))










