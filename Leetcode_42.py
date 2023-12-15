class Solution:
    def trap(self, height: list[int]) -> int:
        if len(height) <= 2:
            return 0
        res = 0
        l, r = 0, 1
        while l < len(height) - 2:
            if height[l] != 0:
                r = l + 1
                inside = 0
                while r < len(height) - 1 and height[r] < height[l]:
                    inside += height[r]
                    r += 1
                if height[r] >= height[l]:
                    res += cal(l, r, height[l], height[r], inside)
                    l = r
                elif height[r] < height[l] and r == len(height) - 1:
                    if l < len(height) - 3:
                        l += 1
                    elif height[l + 1] < height[l] and height[l + 1] < height[r]:
                        res += min(height[l], height[r]) - height[l + 1]
                        l += 1
                    else:
                        break
            else:
                l += 1
        return res


def cal(l, r, heightL, heightR, inside):
    return (r - l - 1) * min(heightL, heightR) - inside