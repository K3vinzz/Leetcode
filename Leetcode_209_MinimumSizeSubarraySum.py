
def minSubArrayLen(target: int, nums: list[int]) -> int:
    l, total = 0, 0
    res = 111111
    for r in range(len(nums)):
        total += nums[r]
        while total >= target:
            res = min(res, r - l + 1)
            total -= nums[l]
            l += 1
    return 0 if res == 111111 else res


print(minSubArrayLen(target=7, nums=[1,1,1,1,7]))





